#!/usr/bin/python
import os
import datetime

date = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
note_xml_template = """<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export2.dtd"><en-export export-date="%(date)s" application="Catch" version="">%(notes)s</en-export>"""

def write_enex(source_dir, notes_xml):
	folder_naming_file_name = source_dir + ".enex"
	folder_naming_file = open(folder_naming_file_name, "w")
	folder_naming_file.write(notes_xml)
	folder_naming_file.close()
	return folder_naming_file_name

def prepcatch():
	source_dir = "All Notes"
	dirs = [dir for dir in os.listdir(".") if os.path.isdir(dir)]
	if source_dir not in dirs:
		print "I did not see an %s subdirectory, \nplease run the script within the top folder of the Catch Notes.zip extract" % source_dir
		return
	
	for source_dir in dirs:
		notes = []
		note_dirs = [dir for dir in os.listdir(source_dir) \
				if os.path.isdir(os.path.join(source_dir, dir))]
		for dir in note_dirs:
			source_file = os.path.join(source_dir, dir, "note.enex")
			note_file = open(source_file)
			note_xml = note_file.read()
			note_file.close()
			note_xml = note_xml[note_xml.index("<note>"):note_xml.index("</note>") + len("</note>")]
			notes.append(note_xml)
		notes_xml = note_xml_template % {"notes": "".join(notes), "date" : date }
		target_file = write_enex(source_dir, notes_xml)

		print "Copied %s notes into %s" % (len(note_dirs), target_file)

if __name__ == "__main__":
	prepcatch()
