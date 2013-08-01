# Prep Catch Zip for Evernote Desktop

This is a python script to help ease the transistion from Catch Notes to Evernote.

In the Catch Notes Archive, each Space has its own directory. Within each Space, each note is placed in its own directory. To import them into Evernote, you have to select each note individually.
  
The script, for each space, creates a folder called "{Space Name} Import", and copies all those nested note.enex files into it so you can import your .enex files into Evernote Desktop with one upload action per Space. 

## Mac/Linux Instructions

* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Unzip
* Download this project's zip file at https://github.com/davious/PrepCatchZipForEvernoteDesktop/archive/master.zip
* Unzip

```
cd ~/Downloads/Catch Notes/
~/Downloads/PrepCatchZipForEvernoteDesktop-master/prepcatch.py
Copied 100 notes into All Notes Import directory.
Copied 60 notes into Space One Import directory.
Copied 40 notes into Space Two Import directory.
```

## Details

Here is what I do to switch from Catch to Evernote
 
* Logged into Catch.com
* Under my username, upper right, I select the Export menu item (https://catch.com/tools/export/new)
* I click on the Zip Archive File button, under Download
* I extract the Zip File
* Using the command line, I go to the "Catch Notes" directory I just extracted
* I run prepcatch.py
* In the Evernote Desktop app, for each Space
    * File > Import
    * Open the "Catch Notes" directory
    * Open the space's Import directory
    * Select all the files using cntl-a or, for mac, command-a
    * Click Open
* Done

