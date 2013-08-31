#!/usr/bin/python
import os
import sys
import re
import datetime
import time
from time import sleep

import zipfile
import hashlib
import binascii
import mimetypes

from lxml import etree

import evernote.edam.type.ttypes as Types
from evernote.api.client import EvernoteClient
from evernote.api.client import NoteStore
from evernote.edam.error.ttypes import EDAMSystemException
from evernote.edam.error.ttypes import EDAMUserException



bad_title_name = "Note with removed title"

def plunk(_):
	sys.stdout.write(_)
	sys.stdout.flush()

def bale(note_file, e):
	print "Sorry, I could not import note %s" % note_file.note
	print " Error Message is " + str(e)
	print " skipping..."

def get_zip_file_name():
	zip_file_names = [zip_file_name for zip_file_name in os.listdir(".") \
					  if zip_file_name.startswith("Catch Notes") \
					  and zip_file_name.endswith(".zip")]
	if not len(zip_file_names):
		return None
	return zip_file_names[0]

def extract_tags(content):
	tags = re.findall(r'\B#\w+', content)
	tags = list(set(tags))
	return [tag[1:] for tag in tags]

def get_milliseconds_from_utc(utc):
	dt = datetime.datetime.strptime(utc, "%Y%m%dT%H%M%SZ")
	return int(time.mktime(dt.timetuple())) * 1000

def pause(seconds):
	print
	seconds += 10
	while seconds:
		plunk("pushing data too fast for evernote, pausing for %s minutes and %s seconds      \r" % (seconds/60, seconds % 60))
		sleep(1)
		seconds -= 1
	print

class NoteAlreadyExists(Exception):
	pass

class NoteFile:
	def __init__(self, file_name):
		self.full_name = file_name
		self.paths = file_name.split('/')
		if len(self.paths) < 4:
			raise Exception("not a note path: " + file_name)
		if 'spaces' in self.paths:
			# Catch Notes/spaces/All Notes/filename
			self.space = self.paths[self.paths.index('spaces') + 1]
		else:
			self.space = self.paths[1]
		if 'notes' in self.paths:
			# Catch Notes/spaces/All Notes/notes/My note/filename
			self.note = self.paths[self.paths.index('notes') + 1]
		else:
			self.note = self.paths[2]
		self.file = self.paths[-1]
		if self.file in ("note.txt", "note.html"):
			raise Exception(self.file + " files are not considered NoteFiles: " + file_name)
		if self.file in ("notes.txt", "notes.html", "notes.enex"):
			raise Exception("Not interested in notes files: " + file_name)
		if self.file == "note.enex" and self.space == "All Notes":
			raise Exception("Not interested in All Notes note.enex files: " + file_name)

class NoteImporter:
	def __init__(self, token):
		self.token = token
		for sandbox in (True, False):
			self.sandbox = sandbox
			self.client = EvernoteClient(token=token, sandbox=sandbox)
			try:
				self.note_store = self.client.get_note_store()
				self.notebooks = self.note_store.listNotebooks()
				break
			except EDAMSystemException as e:
				if e.errorCode == 19:
					pause(e.rateLimitDuration)
			except:
				if not sandbox:
					print "Trouble accessing your evernote account with the provided developer token: '%s'" % token
					raise
		zip_file_name = get_zip_file_name()
		if not zip_file_name:
			raise Exception("I did not see an Catch Notes .zip file,\n please run the script in the directory of the exported Catch Notes .zip file")
		self.zip_file = zipfile.ZipFile(zip_file_name, "r")
		self.space_files = self.get_space_files()
		self.already_createds = {}

	def set_already_createds_for_notebook(self, guid):
		filter = NoteStore.NoteFilter()
		filter.notebookGuid = guid
		spec = NoteStore.NotesMetadataResultSpec()
		spec.includeCreated = True

		note_start = 0
		max_notes = 250
		createds = []
		while True:
			noteinfos = self.note_store.findNotesMetadata(filter, note_start, note_start + max_notes, spec)
			if not len(noteinfos.notes):
				break
			createds.extend([noteinfo.created for noteinfo in noteinfos.notes])
			note_start += max_notes

		self.already_createds[guid] = {}
		for created in createds:
			self.already_createds[guid][created] = True
		
	def get_space_files(self):
		space_files = {}
		for file_name in self.zip_file.namelist():
			try:
				note_file = NoteFile(file_name)
			except Exception as rejection:
				continue
			if not note_file.space in space_files:
				space_files[note_file.space] = {}
			if not note_file.note in space_files[note_file.space]:
				space_files[note_file.space][note_file.note] = []
			space_files[note_file.space][note_file.note].append(note_file)
		return space_files

	def create_notebook(self, space):
		existing_notebooks = [notebook for notebook in self.notebooks if space == notebook.name]
		if len(existing_notebooks):
			self.set_already_createds_for_notebook(existing_notebooks[0].guid)
			return existing_notebooks[0].guid, False
		notebook = Types.Notebook()
		notebook.name = space
		notebook = self.note_store.createNotebook(notebook)
		return notebook.guid, True

	def create_note(self, notebook_guid, note_file, attachments, title_override=None):
		data = self.zip_file.read(note_file.full_name)
		info = etree.fromstring(data)
		note = Types.Note()
		note.notebookGuid = notebook_guid
		note.title = title_override or \
			info.xpath("//note/title")[0].text.replace("\t", " ").strip().encode('utf-8')
		note.created = get_milliseconds_from_utc(info.xpath("//note/created")[0].text)
		note.updated = get_milliseconds_from_utc(info.xpath("//note/updated")[0].text)
		note.attributes = Types.NoteAttributes()
		note.attributes.author = info.xpath("//note/note-attributes/author")[0].text.encode('utf-8')

		content = info.xpath("//note/content")[0].text
		
		if notebook_guid in self.already_createds \
		   and note.created in self.already_createds[notebook_guid]:
			plunk('"')
			raise NoteAlreadyExists
		
		plunk(".")
		
		if len(attachments):
			plunk("@")
			note.resources = [self.create_attachment(attachment) \
							for attachment in attachments]
			attachment_xml = "<br /><br />"
			for attachment in note.resources:
				hash_hex = binascii.hexlify(attachment.data.bodyHash)
				attachment_xml += '<en-media type="%s" hash="%s"/>' % (attachment.mime, hash_hex)
			content = content.replace("</en-note>", attachment_xml + "</en-note>")
		note.content = content.encode('utf-8')
		note.tagNames = extract_tags(content)
		if len(note.tagNames):
			plunk("#")

		self.note_store.createNote(note)
		return note

	def create_attachment(self, attachment_note_file):
		file_data = self.zip_file.read(attachment_note_file.full_name)

		md5 = hashlib.md5()
		md5.update(file_data)
		hash = md5.digest()

		data = Types.Data()
		data.size = len(file_data)
		data.bodyHash = hash
		data.body = file_data

		resource = Types.Resource()
		resource.data = data
		resource.fileName = attachment_note_file.file
		resource.mime = mimetypes.guess_type(resource.fileName)[0]
		if resource.fileName.endswith("3gpp"):
			resource.mime = "audio/3gpp"
		if resource.fileName.endswith("mp4"):
			resource.mime = "audio/mp4"
		return resource

	def import_notes_into_evernote(self):
		space_files = self.space_files
		space_file_list = sorted(space_files.iterkeys())
		for space in space_file_list:
			if space == "All Notes":
				continue
			
			notebook_guid, is_new = self.create_notebook(space)
			action = "Created" if is_new else "Continuing with"

			print "%s '%s' Notebook and uploading its %s notes..." \
					% (action, space, len(space_files[space]))

			counter = 0
			total_attachments = 0
			total_tags = 0
			note_files = space_files[space]
			note_list = sorted(note_files.iterkeys())
			for note in note_list:
				if counter:
					if counter % 5 == 0:
						plunk(" ")
					if counter % 25 == 0:
						print
					if counter % 100 == 0:
						print
				counter += 1
				note_file = note_files[note][0]
				attachments = []
				if "All Notes" in space_files and note in space_files["All Notes"]:
					attachments = space_files["All Notes"][note]
					total_attachments += len(attachments)
				try:
					created_note = self.create_note(notebook_guid, note_file, attachments)
				except NoteAlreadyExists:
					continue
				except EDAMUserException as e:
					if e.errorCode == 2:
						print
						print "had trouble with title for note %s\n trying with '%s'" \
							% (note_file.note, bad_title_name)
						created_note = self.create_note(notebook_guid, note_file, attachments, title_override=bad_title_name)
					else:
						bale(note_file, e)
						continue
				except EDAMSystemException as e:		
					if e.errorCode == 19:
						pause(e.rateLimitDuration)
						created_note = self.create_note(notebook_guid, note_file, attachments)
					else:
						bale(note_file, e)
						continue
				
				if len(created_note.tagNames):
					total_tags += len(created_note.tagNames)
				
			print
			message = "Completed '%s' Notebook upload: uploaded %s notes" % (space, len(space_files[space]))
			if total_attachments:
				message += ", %s attachments" % total_attachments
			if total_tags:
				message += ", %s tags" % total_tags
			print message
			print

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Please include your developer token on the command line"
	else:
		note_importer = NoteImporter(sys.argv[1])
		note_importer.import_notes_into_evernote()


