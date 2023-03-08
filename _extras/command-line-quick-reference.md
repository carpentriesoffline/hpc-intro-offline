---
title: Command Line Cheat Sheet
---

## Linux Command Line Cheat Sheet
HPCs will be based on linux systems and the main way that you interact with them is through the command line. Here is a quick reminder of common commands that you will need:

`ls` list what is in the current directory

`ls path/to/folder` list what is in the directory you have given the path to.

`ls -a` list what is in the current directory including hidden files

`cd path/to/folder` change directory to the specified folder

`cd ..` change directory to the folder above the current folder

`pwd` print the file path of the current working directory (to find out where you are)

`cp file1 file2` Make a copy of a file, in this example copy file1 and create a duplicate called file2. You can give a full file path to make a copy in a different location.

`mv file1 new/location/file1` Move a file, in this case file 1 is moved to a new location in a subfolder.

`mv file1 file2` If you move a file to the same directory, this will act to rename the file. This example will rename file1 to file2.

`curl weblink` download contents from a given location on the internet, replace 'weblink' with the location.

`wget weblink` download contents from a given location on the internet - this is not available on windows by default. An alternative to curl.

`nano filename` Open a file with the text editor nano. NB: nano commands are shown in the nano screen, with a '^' meaning ctrl. E.g. ^x to exit means press ctrl x to exit. 


## Windows PowerShell Cheat Sheet
If you are using windows and don't have a linux command line option available (e.g. git bash or linux subsystem for windows) then you can launch the windows powershell by searching programs for 'cmd'. The below is a quick cheat sheet for common commands for using the windows power shell:

`dir` list what is in the current directory

`cd` as with linux, this will let you change directory

`notepad filename` nano is not installed by default on windows so if you need to edit a document from the powershell command line you will need to use notepad, unless you have an alternative installed.
