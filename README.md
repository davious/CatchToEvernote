# Prep Catch Zip for Evernote Desktop

This is a python script to help ease the transistion from Catch Notes to Evernote.

The script copies all note.enex files in the "All Notes" directory of a Catch Note Archive into a "All Notes Gathered" directory.

This allows you to select all your enex files for import into Evernote Desktop in one go. 

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
