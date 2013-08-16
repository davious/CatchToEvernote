# Catch To Evernote

This is a couple of python scripts to transition from Catch to Evernote.

## autocatch

This script automatically loads all your notes from your Catch Notes.zip.

This script requires you to use your developer token provided by Evernote. You can find it at https://www.evernote.com/api/DeveloperToken.action

A developer token looks like this

```
S=s27:U=2df34c:E=147d74d2653:C=1407f9bfa57:P=1cd:A=en-devtoken:V=2:H=ba73ea24eff00593b64a9d6a0163fc3e
```

You can test this script against a sandbox account. To get a sandbox developer account and token, create an account at https://sandbox.evernote.com/ and then go to https://sandbox.evernote.com/api/DeveloperToken.action

This script also requires a couple python packages to be installed: evernote and lxml

### Details

Here is what I do to switch from Catch to Evernote
 
* Log into Catch.com
* Under my username, upper right, I select the Export menu item (https://catch.com/tools/export/new)
* Using the command line, I go to Downloads directory
* I run autocatch.py

### symbol legend

Update progress is indicated by symbols

* ``.`` = note added
* ``@`` = attachment(s) with note
* ``#`` = tags(s) with note
* ``"`` = note already exists from a previous import attempt


### Mac/Linux Instructions

#### Install python packages
```
sudo easy_install evernote lxml
```

Note: On a mac, if you have trouble with the lxml easy_install, see http://stackoverflow.com/questions/8473066/gcc-4-2-failed-with-exit-status-1

#### Download Catch Export and this script
* Download Catch Archive Zip File at https://catch.com/tools/export/new
    * no need to unzip
* Download and unzip this project's zip file at https://github.com/davious/CatchToEvernote/archive/master.zip

#### run autocatch
```
cd ~/Downloads/
CatchToEvernote-master/autocatch.py <developer token>
Added 'Space 1' Notebook and uploading its 15 notes...
..... .@.@#...# ..@... 
Completed 'Space 1' Notebook upload: uploaded 15 notes, 3 attachments, 2 tags
Added 'Space 2' Notebook and uploading its 10 notes...
.#.@#..@.# .@.#.@#..
Completed 'Space 2' Notebook upload: uploaded 10 notes, 5 attachments, 25 tags
```

### PC Instructions

#### Install python and additional python packages
* Install Python http://python.org/download/ [Windows 64bit (newer computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi) or [Windows 32bit (older computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.msi)
* Install additional python packages
```
C:\Python27\Scripts\easy_install evernote lxml
```

#### Download Catch Export and this script
* Download Catch Archive Zip File at https://catch.com/tools/export/new
    * No need to unzip
* Download and unzip this project's zip file at https://github.com/davious/CatchToEvernote/archive/master.zip

#### run autocatch

Run cmd
```
cd C:\Users\yourusername\Downloads\
C:\Python27\python C:\Users\yourusername\Downloads\CatchToEvernote\CatchToEvernote-master\autocatch.py <developer token>
Added 'Space 1' Notebook and uploading its 15 notes...
..... .@.@#...# ..@... 
Completed 'Space 1' Notebook upload: uploaded 15 notes, 3 attachments, 2 tags
Added 'Space 2' Notebook and uploading its 10 notes...
.#.@#..@.# .@.#.@#..
Completed 'Space 2' Notebook upload: uploaded 10 notes, 5 attachments, 25 tags
```

## prepcatch

This was an earlier used script, recommended for people who don't have a lot of attachments or who don't want to use a developer token.

The script works on your unextracted Catch Notes Export.zip file and creates a custom extract folder.

The in resulting extracted Extract folder there are the following:
* An "All Notes.enex"
* A {Space}.enex file, per space
* An attachments folder with all your attachments with the title of the note as the file name. This way you can look at the file name, type the title into evernote search and re-attach the attachment to the related note.

### Details

Here is what I do to switch from Catch to Evernote
 
* Log into Catch.com
* Under my username, upper right, I select the Export menu item (https://catch.com/tools/export/new)
* Using the command line, I go to Downloads directory
* I run prepcatch.py
* In the Evernote Desktop app, for each Space
    * File > Import
    * Go into the Catch Notes Extract folder the script creates
    * Select the .enex file with the space's name
    * Click Open
    * Done
* Attachments
    * Go into the Catch Notes Extract > Attachments folder the script creates
    * Type the name of the note (from the file name) into the evernote desktop search
    * Drag-and-drop the attachment into the note
    * Delete the attachment from the Attachment folder


### Mac/Linux Instructions

* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Download this project's zip file at https://github.com/davious/CatchToEvernote/archive/master.zip
* Unzip

```
cd ~/Downloads
CatchToEvernote-master/prepcatch.py
Extracted 1 All Notes.enex file and 6 {Space}.enex files into Catch Notes username exported 2013-8-1 Extract
Extracted 212 attachments into Catch Notes username exported 2013-8-1 Extract/Attachments.
```

### PC Instructions

* Install Python http://python.org/download/ [Windows 64bit (newer computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi) or [Windows 32bit (older computers)](http://python.org/ftp/python/2.7.5/python-2.7.5.msi)
* Download Catch Archive Zip File at https://catch.com/tools/export/new
* Download this project's zip file at https://github.com/davious/CatchToEvernote/archive/master.zip
* Unzip

Run cmd
```
cd C:\Users\yourusername\Downloads\
C:\Python27\python C:\Users\yourusername\Downloads\CatchToEvernote-master\CatchToEvernote-master\prepcatch.py
Extracted 1 All Notes.enex file and 6 {Space}.enex files into Catch Notes username exported 2013-8-1 Extract
Extracted 212 attachments into Catch Notes username exported 2013-8-1 Extract/Attachments.
```

