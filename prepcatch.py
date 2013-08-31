#!/usr/bin/python
import os
import zipfile
import re

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def write_file(target_file, data):
	ensure_dir(target_file)
	target_file = open(target_file, "w")
	target_file.write(data)
	target_file.close()

def prepcatch():
	zip_file_names = [zip_file_name for zip_file_name in os.listdir(".") \
					if zip_file_name.startswith("Catch Notes") \
					and zip_file_name.endswith(".zip")]
	
	if not len(zip_file_names):
		print "I did not see an Catch Notes .zip file,\n please run the script in the directory of the exported Catch Notes .zip file"
	
	zip_file_name = zip_file_names[0]
	export_dir = zip_file_name[:-4] + " Extract"
	os.mkdir(export_dir)

	zip_file = zipfile.ZipFile(zip_file_name, "r")

	space_files = [file_name for file_name in zip_file.namelist() if file_name.endswith("notes.enex")]
	for space_file in space_files:
		data = zip_file.read(space_file)
		paths = space_file.split('/')
		space = paths[2] if paths[1] == "spaces" else paths[1]
		target_file = os.path.join(export_dir, space + ".enex")
		write_file(target_file, data)

	print "Extracted 1 All Notes.enex file and %s {Space}.enex files into %s" % (len(space_files) - 1, export_dir)

	attachments = [file_name for file_name in zip_file.namelist() \
					if not (file_name.endswith(".html") \
					 or file_name.endswith(".enex") \
					 or file_name.endswith(".txt"))]
	export_dir = os.path.join(export_dir, "Attachments")
	if attachments:
		os.mkdir(export_dir)
	for attachment in attachments:
		data = zip_file.read(attachment)
		paths = attachment.split('/')
		target_file = os.path.join(export_dir, paths[-2] + paths[-1][paths[-1].find('.'):])
		write_file(target_file, data)
	if attachments:
		print "Extracted %s attachments into %s" % (len(attachments), export_dir)

if __name__ == "__main__":
	prepcatch()
