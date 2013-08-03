#!/usr/bin/python
import os
import zipfile

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def prepcatch():
	zip_file_names = [zip_file_name for zip_file_name in os.listdir(".") \
					if zip_file_name.startswith("Catch Notes") \
					and zip_file_name.endswith(".zip")]
	
	if not len(zip_file_names):
		print "I did not see an Catch Notes .zip file,\n please run the script in the directory of the exported Catch Notes .zip file"
	
	zip_file_name = zip_file_names[0]
	export_dir = zip_file_name[:-4] + " Attachments"
	os.mkdir(export_dir)

	zip_file = zipfile.ZipFile(zip_file_name, "r")

	attachments = [file_name for file_name in zip_file.namelist() \
			   if not (file_name.endswith(".html") \
					 or file_name.endswith(".enex") \
					 or file_name.endswith(".txt"))]
	for attachment in attachments:
		data = zip_file.read(attachment)
		paths = attachment.split(os.sep)
		target_file = os.path.join(export_dir, paths[2] + paths[3][paths[3].find('.'):])
		ensure_dir(target_file)
		target_file = open(target_file, "w")
		target_file.write(data)
		target_file.close()

	print "Copied %s attachments into %s" % (len(attachments), export_dir)

if __name__ == "__main__":
	prepcatch()
