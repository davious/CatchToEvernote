# Prep Catch Zip for Evernote Desktop

This is a python script to help ease the transition from Catch Notes to Evernote.

In the Catch Notes Archive, each Space has its own directory. Within each Space, each note is placed in its own directory. To import them into Evernote, you have to select each note individually.
  
The script, for each space, creates a .enex file and copies all those nested note.enex files into it so you can import notes into Evernote Desktop with one upload action per Space. 

## Details

Here is what I do to switch from Catch to Evernote
 
* Log into Catch.com
* Under my username, upper right, I select the Export menu item (https://catch.com/tools/export/new)
* I click on the Zip Archive File button, under Download
* I extract the Zip File
* Using the command line, I go to the "Catch Notes" directory I just extracted
* I run prepcatch.py
* In the Evernote Desktop app, for each Space
    * File > Import
    * Select the .enex file with the space's name
    * Click Open
    * Done


## Mac/Linux Instructions

* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Unzip
* Download this project's zip file at https://github.com/davious/PrepCatchZipForEvernoteDesktop/archive/master.zip
* Unzip

```
cd ~/Downloads/Catch Notes/
~/Downloads/PrepCatchZipForEvernoteDesktop-master/prepcatch.py
Copied 100 notes into All Notes.enex
Copied 60 notes into Space One.enex
Copied 40 notes into Space Two.enex
```

## PC Instructions

* Install Python http://python.org/download/ [Windows 64bit (newer computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi) or [Windows 32bit (older computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.msi)
* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Unzip
* Download this project's zip file at https://github.com/davious/PrepCatchZipForEvernoteDesktop/archive/master.zip
* Unzip

Run cmd
```
cd C:\Users\yourusername\Downloads\Catch Notes Full Name\Catch Notes\
C:\Python27\python C:\Users\yourusername\Downloads\PrepCatchZipForEvernoteDesktop-master\PrepCatchZipForEvernoteDesktop-master\prepcatch.py
Copied 100 notes into All Notes.enex
Copied 60 notes into Space One.enex
Copied 40 notes into Space Two.enex
```

