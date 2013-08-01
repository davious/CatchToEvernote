#!/usr/bin/python
import os
import shutil
import datetime

def prepcatch():
	source_dir = "All Notes"
	target_dir = "All Notes Gathered"
	folder_naming_file_name = " Catch Notes.enex"
	dirs = os.listdir('.')
	if source_dir not in dirs:
		print "I did not see an %s subdirectory, \nplease run the script within the top folder of the Catch Notes.zip extract" % source_dir
		return
	
	os.mkdir(target_dir)

	folder_naming_file = open(os.path.join(target_dir, folder_naming_file_name), "w")
	date = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
	note_xml = """<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export2.dtd"><en-export export-date="%" application="Catch" version=""><note><title>Imported Catch Notes</title><content><![CDATA[<?xml version="1.0" encoding="UTF-8" standalone="no"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note style="word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;"><div>This note used to name the import folder</div></en-note>]]></content><created>%(date)s</created><updated>%(date)s</updated><note-attributes><author>PrepCatchNotesForEvernoteImport</author></note-attributes></note></en-export>"""
	folder_naming_file.write(note_xml)
	folder_naming_file.close()

	dirs = [dir for dir in os.listdir(source_dir) \
			if os.path.isdir(os.path.join(source_dir, dir))]
	for dir in dirs:
		source_file = os.path.join(source_dir, dir, "note.enex")
		target_file = os.path.join(target_dir, dir + ".enex")
		shutil.copy2(source_file, target_file)

	print "Copied %s notes into %s directory." % (len(dirs), target_dir)
	print " Added '%s' to have Evernote start with a nice folder name." % (folder_naming_file_name)

if __name__ == "__main__":
	prepcatch()
