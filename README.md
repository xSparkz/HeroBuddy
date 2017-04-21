# Hero-Buddy
Minecraft Tool written in Python to Generate Heroes for Malons SuperHero Server

AUTHOR
=======

xSp4rkz (https://namemc.com/profile/xSp4rkz.1)


SERVER
======

Server Address: mynecraft.servegame.com
Owner: God_Doesnt_Exist (https://namemc.com/profile/God_Doesnt_Exist.2)

Hero Buddy was built for developing heroes for this server.


DEPENDENCIES
============
Python 2.7

(1) sudo apt-get install python-mechanize python-qt4


MAKING CHANGES TO GUI
=====================

If you would like to make changes to the GUI (gui.ui) you will need to install QT Designer and dev tools:

(1) sudo apt-get install qt4-designer pyqt4-dev-tools
(2) Open (gui.ui) using 'Qt 4 Designer' and make the changes you'd like
(3) Save changes
(4) Open terminal and navigate to folder where gui.ui is located
(5) Execute command in step six to compile the gui.ui into python code (gui.py)
(6) pyuic4 gui.ui -o gui.py


HOW TO RUN
==========

python main.py


HOW TO USE
==========

(1) Watch the video tutorials on http://mynecraft.servegame.com/howtomakeahero.html to understand how a hero is created
(2) Using the knowledge you obtained through the video tutorials you can now use Hero-Buddy which will assist you in creating the files for you
(3) Run the program and fill out all the required information.
(4) Go to the Build Tab and click the 'Create Hero' button
(5) Select or create a new folder where the hero files will be created. The software will automatically create the correct folder structure
(6) Take the files that were created and add them to https://github.com/malonnnn/ServerConfig by creating a new pull request

NOTE: The software takes the texture information from the supplied PlayerName. In order to set the correct texture you must switch
your texture prior to using the software.

Enjoy!!