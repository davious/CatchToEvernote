#!/usr/bin/env python
import os
import shutil

def prepcatch():
	source_dir = "All Notes"
	target_dir = "All Notes Gathered"
	dirs = os.listdir('.')
	if source_dir not in dirs:
		print "I did not see an %s subdirectory, \nplease run the script within the top folder of the Catch Notes.zip extract" % source_dir
		return
	os.mkdir(target_dir)
	dirs = [dir for dir in os.listdir(source_dir) \
			if os.path.isdir(os.path.join(source_dir, dir))]
	for dir in dirs:
		source_file = os.path.join(source_dir, dir, "note.enex")
		target_file = os.path.join(target_dir, dir + ".enex")
		shutil.copy2(source_file, target_file)
	print "Copied %s notes into %s" % (len(dirs), target_dir)

if __name__ == "__main__":
	prepcatch()
