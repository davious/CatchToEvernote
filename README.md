# Prep Catch Zip for Evernote Desktop

A python script you execute on a Catch Notes.zip extraction directory.

The script copies all note.enex files to one directory and the file is renamed to the folder name it was located in.

This allows you to select all your enex file in one file-selection action. 

## Mac/Linux Instructions

```
Download Zip File
Unzip

cd ~/Downloads/Catch Notes/
~/Downloads/PrepCatchZipForEvernoteDesktop-master/prepcatch.py
Copied 1219 notes into All Notes Gathered directory.
 Added ' Catch Notes.enex' to have Evernote start with a nice folder name.
```

## Details

Here is what I did to switch from Catch to Evernote
 
* Logged into Catch.com
* Under my username, upper right, I selected the Export menu item
* I ended up at https://catch.com/tools/export/new
* I clicked on the Zip Archive File button, under Download
* Extract the Zip File
* Ran prepcatch.py
* In Evernote Desktop
* File > Import
* Locate the "All Notes Gathered" directory in the extracted "Catch Notes" directory
* Selected all the files using cntl-a or, for mac, command-a
* Clicked Open
* Done
