# Prep Catch Zip Attachments for Evernote Desktop

This is a python script to pick out attachments from Catch Notes to Evernote.

In the Catch Notes Archive Attachments are nested away in there own note directory. To import them into Evernote, you have to hunt through and select each attachment individually.
  
The script, copies each attachment into an Attachments Directory so you have one folder to select attachments from. 

## Details

Here is what I do to switch from Catch to Evernoted
 
* Log into Catch.com
* Under my username, upper right, I select the Export menu item (https://catch.com/tools/export/new)
* I click on the Zip Archive File button, under Download
* I extract the Zip File
* I go into Evernote Desktop and for each space, import the notes.enex file and rename the import folder.
* Using the command line, I go to Downloads directory
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
Copied 212 attachments into Catch Notes username exported 2013-8-1 Attachments.
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
Copied 212 attachments into Catch Notes username exported 2013-8-1 Attachments.
```

