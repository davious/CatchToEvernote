# Prep Catch Zip for Evernote Desktop

This is a python script to pick out notes and attachments from Catch Notes so they'll be ready to import them into Evernote.

The script works on your unextracted Catch Notes Export.zip file and creates a custom extract folder.

The in resulting extracted Extract folder there are the following:
* An "All Notes.enex"
* A {Space}.enex file, per space
* An attachments folder with all your attachments with the title of the note as the file name. This way you can look at the file name, type the title into evernote search and re-attach the attachment to the related note.

## Details

Here is what I do to switch from Catch to Evernoted
 
* Log into Catch.com
* Under my username, upper right, I select the Export menu item (https://catch.com/tools/export/new)
* I click on the Zip Archive File button, under Download
* Using the command line, I go to Downloads directory
* I run prepcatch.py
* In the Evernote Desktop app, for each Space
    * File > Import
    * Go into the Catch Notes Import folder the script creates
    * Select the .enex file with the space's name
    * Click Open
    * Done
* Attachments
    * Go into the Catch Notes Import > Attachments folder the script creates
    * Type the name of the note (from the file name) into the evernote desktop search
    * Drag-and-drop the attachment into the note
    * Delete the attachment from the Attachment folder


## Mac/Linux Instructions

* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Download this project's zip file at https://github.com/davious/PrepCatchZipForEvernoteDesktop/archive/master.zip
* Unzip

```
cd ~/Downloads/Catch Notes/
~/Downloads/PrepCatchZipForEvernoteDesktop-master/prepcatch.py
Extracted 1 All Notes.enex file and 6 {Space}.enex files into Catch Notes username exported 2013-8-1 Extract
Extracted 212 attachments into Catch Notes username exported 2013-8-1 Import/Attachments.
```

## PC Instructions

* Install Python http://python.org/download/ [Windows 64bit (newer computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi) or [Windows 32bit (older computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.msi)
* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Download this project's zip file at https://github.com/davious/PrepCatchZipForEvernoteDesktop/archive/master.zip
* Unzip

Run cmd
```
cd C:\Users\yourusername\Downloads\Catch Notes Full Name\Catch Notes\
C:\Python27\python C:\Users\yourusername\Downloads\PrepCatchZipForEvernoteDesktop-master\PrepCatchZipForEvernoteDesktop-master\prepcatch.py
Extracted 1 All Notes.enex file and 6 {Space}.enex files into Catch Notes username exported 2013-8-1 Extract
Extracted 212 attachments into Catch Notes username exported 2013-8-1 Import/Attachments.
```

