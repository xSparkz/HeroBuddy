# This file is part of Hero Buddy.

#Hero Buddy is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#Hero Buddy is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with Hero Buddy.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'xSp4rkz'

import webcrawler # Functions to interact with internet such as obtaining users UUID or skin information
import sys # Used to supply argv to application
import gui # All of the GUI code independent from functional code
from PyQt4 import QtGui # Library for working with GUI
from PyQt4.QtCore import QObject # Used to work with Gui Objects
from common import *
import os # Used to manipulate files and folders

class HeroBuddyGui(QtGui.QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(HeroBuddyGui, self).__init__(parent)
        self.setupUi(self)

class Application(QObject):

    def __init__(self):

        QObject.__init__(self)  # initialisation required for object inheritance

        self.MainApp = QtGui.QApplication(sys.argv) # Setup main application
        self.MainWindow = HeroBuddyGui() # Setup main window

        self.Website = webcrawler.WWWConnection() # Object used to communicate with different websites to extract data

        # Variables
        self.UUID = '' # Used to store the UUID so that it can be referenced later
        self.Signature = '' # Used to store the Signature so that it can be referenced later
        self.Value = '' # Used to store the Value so that it can be referenced later
        self.HeroesName = '' # Used to store the Heroes name so it can be referenced later

        # Connect website output to the GUI
        self.Website.ConnectGUI(self.MainWindow.listStatus)

        # Populate Text Boxes
        # (1) Available Permissions
        HeroPermissions = self.Website.GetHeroPermissions() # Grab the permissions from Malons Github account
        self.__CopyListToListView(HeroPermissions, self.MainWindow.listPermissions) # Copy the permissions to the permissions list

        # (2) Effects
        self.__CopyFileToText(FILE_EFFECTS, self.MainWindow.txtEffects) # Open file and read contents into destination

        # (3) Blocks and Items
        self.__CopyFileToText(FILE_BLOCKS_AND_ITEMS, self.MainWindow.txtBlocks) # Open file and read contents into destination

        # (4) Enchantments
        self.__CopyFileToText(FILE_ENCHANTMENTS, self.MainWindow.txtEnchantments) # Open file and read contents into destination

        # (5) Trails
        self.__CopyFileToListView(FILE_TRAILS, self.MainWindow.listTrails) # Open file and read contents into destination

        # Setup bindings
        # Connect buttons to Callback Functions
        self.MainWindow.btnCloneToHeroName.clicked.connect(self.ButtonClick_Clone)
        self.MainWindow.btnCloneToHeroesSpeech.clicked.connect(self.ButtonClick_Clone)
        self.MainWindow.btnCloneToHeroesChatColor.clicked.connect(self.ButtonClick_Clone)
        self.MainWindow.btnClearScratchPad.clicked.connect(self.ButtonClick_ClearScratchPad)
        self.MainWindow.btnUsePlayerName.clicked.connect(self.ButtonClick_UsePlayerName)
        self.MainWindow.btnLoadBuffsExample.clicked.connect(self.ButtonClick_LoadExample)
        self.MainWindow.btnLoadPowersExample.clicked.connect(self.ButtonClick_LoadExample)
        self.MainWindow.btnCreate.clicked.connect(self.ButtonClick_Build)

        #Bukkit Color Code Buttons
        self.MainWindow.btnColor_1.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_2.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_3.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_4.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_5.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_6.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_7.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_8.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_9.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_10.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_11.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_12.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_13.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_14.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_15.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_16.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_17.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_18.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_19.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_20.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_21.clicked.connect(self.ButtonClick_Color)
        self.MainWindow.btnColor_22.clicked.connect(self.ButtonClick_Color)

    # All Color buttons are responsible for grabbing the corresponding Bukkit Color code
    # and inserting that code into the scratch pad on the Colors tab
    # Helps with building a Heroes Name
    def ButtonClick_Color(self):

        Button = self.sender().objectName() # Store the name of the button that was clicked
        ColorCode = None # Store color code to use

        if Button == 'btnColor_1':
            ColorCode = COLOR_1

        elif Button == 'btnColor_2':
            ColorCode = COLOR_2

        elif Button == 'btnColor_3':
            ColorCode = COLOR_3

        elif Button == 'btnColor_4':
            ColorCode = COLOR_4

        elif Button == 'btnColor_5':
            ColorCode = COLOR_5

        elif Button == 'btnColor_6':
            ColorCode = COLOR_6

        elif Button == 'btnColor_7':
            ColorCode = COLOR_7

        elif Button == 'btnColor_8':
            ColorCode = COLOR_8

        elif Button == 'btnColor_9':
            ColorCode = COLOR_9

        elif Button == 'btnColor_10':
            ColorCode = COLOR_10

        elif Button == 'btnColor_11':
            ColorCode = COLOR_11

        elif Button == 'btnColor_12':
            ColorCode = COLOR_12

        elif Button == 'btnColor_13':
            ColorCode = COLOR_13

        elif Button == 'btnColor_14':
            ColorCode = COLOR_14

        elif Button == 'btnColor_15':
            ColorCode = COLOR_15

        elif Button == 'btnColor_16':
            ColorCode = COLOR_16

        elif Button == 'btnColor_17':
            ColorCode = COLOR_17

        elif Button == 'btnColor_18':
            ColorCode = COLOR_18

        elif Button == 'btnColor_19':
            ColorCode = COLOR_19

        elif Button == 'btnColor_20':
            ColorCode = COLOR_20

        elif Button == 'btnColor_21':
            ColorCode = COLOR_21

        elif Button == 'btnColor_22':
            ColorCode = COLOR_22

        self.__InsertTxtToTxt(ColorCode, self.MainWindow.txtScratchPad)

    def ButtonClick_UsePlayerName(self):
        # Grabs the UUID along with the Texture Signature and Value from Minecraft websites
        # connected to the PlayerName

        self.__CopyTxtToTxt(self.MainWindow.txtPlayerName, self.MainWindow.txtInfoPlayerName) # Copy the PlayerName to the Player Info Tab
        self.UUID = self.Website.GetUUID(str(self.MainWindow.txtPlayerName.toPlainText())) # Grab UUID
        self.Signature, self.Value = self.Website.GetSignature(self.UUID) # Grab the Signature and Value

        self.Signature = str(self.Signature).replace('\n', '').replace('\r', '') # Remove the newlines
        self.Value = str(self.Value).replace('\n', '').replace('\r', '') # Remove the newlines

        self.MainWindow.txtInfoUUID.setPlainText(self.UUID) # Display the UUID
        self.MainWindow.txtInfoSignature.setPlainText(self.Signature) # Display the Signature
        self.MainWindow.txtInfoValue.setPlainText(self.Value) # Display the Value

    def ButtonClick_Clone(self):

        Button = self.sender().objectName() # Store name of button
        TargetTextbox = None # Textbox Object we are going to clone our text to

        if Button == 'btnCloneToHeroName':
            TargetTextbox = self.MainWindow.txtHeroesFancyName

        elif Button == 'btnCloneToHeroesChatColor':
            TargetTextbox = self.MainWindow.txtChatColor

        elif Button == 'btnCloneToHeroesSpeech':
            TargetTextbox = self.MainWindow.txtSpeech

        self.__CopyTxtToTxt(self.MainWindow.txtScratchPad, TargetTextbox) # Copy the text over


    def ButtonClick_ClearScratchPad(self):

        self.MainWindow.txtScratchPad.clear()

    def ButtonClick_LoadExample(self):

        Button = self.sender().objectName()  # Store name of button

        if Button == 'btnLoadBuffsExample':
            self.__CopyFileToText(FILE_EXAMPLE_BUFFS, self.MainWindow.txtBuffs)

        elif Button == 'btnLoadPowersExample':
            self.__CopyFileToText(FILE_EXAMPLE_POWERS, self.MainWindow.txtPowers)

    def ButtonClick_Build(self):

        Status = self.MainWindow.listStatus  # Pointer to our status window

        Echo('Creating Hero', Status)
        Echo('Checking for Completion', Status)

        if self.__CheckForCompletion(): # Is everything complete?

            Echo('Good to Go!', Status)

            # Make the heroes name lower case so it can be used to create the files
            self.HeroesName = str(self.MainWindow.txtHeroesName.toPlainText()).lower()

            BuildFolder = str(QtGui.QFileDialog.getExistingDirectory()) # Show folder select dialog to select the build folder

            if len(BuildFolder) < 1:
                return # User cancelled or didn't select a folder

            Folders = [] # Create a new list of folders to be created

            Folders.append(BuildFolder + '/' + BUILD_FOLDER_HEROFILE) # Add hero folder path to the list of folders (to be created)
            Folders.append(BuildFolder + '/' + BUILD_FOLDER_PERMISSIONS) # Add permissions folder path to the list of folders (to be created)
            Folders.append(BuildFolder + '/' + BUILD_FOLDER_TEMPLATES) # Add template folder path to the list of folders (to be created)

            for Folder in Folders:

                Echo('Checking if folder exists: ' + Folder, Status)

                if not os.path.exists(Folder): # If the folder doesn't exist:

                    Echo('**CREATE** ' + Folder, Status)
                    os.makedirs(Folder) # Create the folder

            # (1) Permissions File
            Template = open(FILE_TEMPLATE_PERMISSIONS, "r")  # Open file for reading
            File = open(BuildFolder + '/' + BUILD_FILE_PERMISSIONS, 'a') # Open file for appending (keep existing)

            Echo('Creating Permissions.yml file: ', Status)

            for Line in str(Template.read()).split("\n"):  # Split the file into Lines using the newline character and read it Line by Line

                # Check for tags and replace them with the right info
                if '<heroname>' in Line:

                    File.write(str(Line).replace('<heroname>', self.HeroesName) + "\n")
                    continue

                if '<prefix>' in Line:
                    File.write(str(Line).replace('<prefix>', str(self.MainWindow.txtHeroesFancyName.toPlainText())) + "\n")
                    continue

                if '<suffix>' in Line:
                    File.write(str(Line).replace('<suffix>', str(self.MainWindow.txtChatColor.toPlainText())) + "\n")
                    continue

                if '<permissions>' in Line:

                    SelectedPermissions = self.MainWindow.listPermissions.selectedItems() # Get the selected permissions
                    Permissions = [] # Create a new list to place the permissions in

                    for Permission in list(SelectedPermissions): # Iterate through the selected items

                        Permissions.append(str(Permission.text())) # Add selected item to list

                    for Permission in Permissions: # Run through the list of permissions

                        File.write(str(TAB_PERMISSIONS + '- ' + Permission) + "\n") # Write it to the file

                    if len(self.MainWindow.txtHeroPermissions.toPlainText()) > 1: # Check to see if theres anything written in the custom permissions box

                        for Permission in str(self.MainWindow.txtHeroPermissions.toPlainText()).split("\n"): # Split them into a list using the newline character as a token

                            File.write(str(TAB_PERMISSIONS + '- ' + Permission) + "\n") # Write it to the file

                    continue

                File.write(Line + "\n") # No tags were detected so leave the line as is

            File.close()
            Template.close()
            Echo('Done!', Status)

        # (2) Hero File
        Template = open(FILE_TEMPLATE_HERO, "r")  # Open file for reading
        File = open(BuildFolder + '/' + BUILD_FOLDER_HEROFILE + '/' + self.HeroesName + '.ms', 'w')  # Open file for writting

        Echo('Creating Hero.ms file', Status)

        for Line in str(Template.read()).split("\n"):  # Split the file into Lines using the newline character and read it Line by Line

            # Check for tags and replace them with the right info
            if '<heroname>' in Line:
                File.write(str(Line).replace('<heroname>', self.HeroesName) + "\n")
                continue

            if '<fancyname>' in Line:
                File.write(str(Line).replace('<fancyname>', str(self.MainWindow.txtHeroesFancyName.toPlainText())) + "\n")
                continue

            if '<signature>' in Line:
                File.write(str(Line).replace('<signature>', self.Signature) + "\n")
                continue

            if '<value>' in Line:
                File.write(str(Line).replace('<value>', self.Value) + "\n")
                continue

            if '<speech>' in Line:
                File.write(str(Line).replace('<speech>', str(self.MainWindow.txtSpeech.toPlainText())) + "\n")
                continue

            if '<op>' in Line:

                if self.MainWindow.checkBoxOP.isChecked(): # Check if the OP checkbox is checked or not
                    File.write(str(Line).replace('<op>', 'true') + "\n")
                else:
                    File.write(str(Line).replace('<op>', 'false') + "\n")

                continue

            if '<trail>' in Line:

                SelectedTrails = self.MainWindow.listTrails.selectedItems() # Get the selected trails
                Trails = [] # Create a new list to store the trails in
                TrailLine = '' # Will be used to build the final string with the list of trails to be inserted into the file

                for Trail in list(SelectedTrails): # Iterate through the selected items
                    Trails.append(str(Trail.text())) # Add the item to the list of trails

                for Trail in Trails: # Iterate through the trails in the list
                    TrailLine = TrailLine + Trail + ', ' # Add the trail to the final string and append a comma and a space for the next trail

                File.write(str(Line).replace('<trail>', str(TrailLine).strip().strip(',')) + "\n") # Remove the spaces on either end and remove the last comma

                continue

            if '<powers>' in Line:

                Powers = str(self.MainWindow.txtPowers.toPlainText()).split("\n") # Create a list of powers by splitting them into lines
                NumberOfPowers = len(Powers) # Count of Powers

                if NumberOfPowers == 1: # Only 1 (No comma)
                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Powers[0]).strip('\"'))) + "\n")
                    continue

                for index, Power in enumerate(Powers): # Used to keep track of current position within the loop

                    if index == (NumberOfPowers - 1): # Last item in list. Make sure we don't add a comma at the end
                        File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Power).strip('\"'))) + "\n")
                        continue

                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_MULTIPLE).replace('<item>', str(Power).strip('\"'))) + "\n")


                continue

            if '<buffs>' in Line:

                Buffs = str(self.MainWindow.txtBuffs.toPlainText()).split("\n") # Create a list of buffs by splitting them into lines
                NumberOfBuffs = len(Buffs) # Count of Buffs

                if NumberOfBuffs == 1: # Only 1 (no comma)
                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Buffs[0]).strip('\"'))) + "\n")
                    continue

                for index, Buff in enumerate(Buffs): # Used to keep track of current position within the loop

                    if index == (NumberOfBuffs - 1): # Last item in list. Make sure we don't add a comma at the end
                        File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Buff).strip('\"'))) + "\n")
                        continue

                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_MULTIPLE).replace('<item>', str(Buff).strip('\"'))) + "\n")

                continue

            File.write(Line + "\n")

        File.close()
        Template.close()
        Echo('Done!', Status)

        # (3) Templates File
        Template = open(FILE_TEMPLATE_TEMPLATES, "r")  # Open file for reading
        File = open(BuildFolder + '/' + BUILD_FOLDER_TEMPLATES + '/templates.yml', 'a')  # Open file for writting

        Echo('Creating Templates.yml', Status)

        for Line in str(Template.read()).split("\n"):  # Split the file into Lines using the newline character and read it Line by Line

            # Check for tags and replace them with the right info
            if '<heroname>' in Line:
                File.write(str(Line).replace('<heroname>', self.HeroesName) + "\n")
                continue

            if '<signature>' in Line:
                File.write(str(Line).replace('<signature>', self.Signature) + "\n")
                continue

            if '<value>' in Line:
                File.write(str(Line).replace('<value>', self.Value) + "\n")
                continue

            if '<playername_lowercase>' in Line:
                File.write(str(Line).replace('<playername_lowercase>', str(self.MainWindow.txtInfoPlayerName.toPlainText()).lower()) + "\n")
                continue

            File.write(Line + "\n")

        File.close()
        Template.close()

        Echo('Done!', Status)
        Echo('**COMPLETE** Hero has been successfully created!', Status)


    def __CopyTxtToTxt(self, Source, Destination):
        # Take the text from a Source Textbox and Copy it to the Destination Textbox
        # Cuts down on code

        Destination.clear() # Clear the TextBox
        Destination.appendPlainText(Source.toPlainText()) # Add the Text

    def __InsertTxtToTxt(self, Source, Destination):
        # Takes some text and inserts it at the last cursor position

        Destination.insertPlainText(Source) # Insert text onto the same line at the current cursor position

    def __CopyListToTxt(self, List, TextBox):
        # Take a list of items and copy them to a Textbox

        for Item in List:
            TextBox.appendPlainText(Item) # Add item from list to text box

        TextBox.moveCursor(QtGui.QTextCursor.Start) # Move the cursor to the top of the textbox
        TextBox.ensureCursorVisible() # Scroll to cursor

    def __CopyListToListView(self, List, ListView):
        # Take a list of items and copy them to a ListView

        for Item in List:
            ListView.addItem(Item)  # Add item from list to ListView

        ListView.scrollToTop() # Scroll the list to the top

    def __CopyFileToText(self, FileName, TextBox):
        # Take a filename and copy the contents of the file to a Textbox

        TextBox.clear() # Clear the TextBox

        File = open(FileName, "r") # Open file for reading

        for Line in str(File.read()).split("\n"): # Split the file into Lines using the newline character and read it Line by Line
            TextBox.appendPlainText(Line) # Add the line to the Textbox

        TextBox.moveCursor(QtGui.QTextCursor.Start)  #Move the cursor to the top of the textbox
        TextBox.ensureCursorVisible()  # Scroll to cursor

        File.close() # Close the file

    def __CopyFileToListView(self, FileName, ListView):
        # Take a filename and copy the contents of the file to a ListView

        ListView.clear() # Clear the ListView

        File = open(FileName, "r")  # Open file for reading

        for Line in str(File.read()).split("\n"):  # Split the file into Lines using the newline character and read it Line by Line
            ListView.addItem(Line)  # Add the line to the ListView

        ListView.scrollToTop() # Scroll the list to the top

        File.close() # Close the file

    def __CheckForCompletion(self):
        # Checks to make sure all the proper TextBoxes are completed and all the proper information is availabe to create a hero file

        MainWindow = self.MainWindow
        Status = self.MainWindow.listStatus

        if not len(MainWindow.txtInfoSignature.toPlainText()):

            Echo('**MISSING** Player Information. Input a PlayerName and click USE', Status)
            return False # Incomplete

        if not len(MainWindow.txtHeroesName.toPlainText()):
            Echo('**MISSING** Heroes Name', Status)
            return False  # Incomplete

        if ' ' in MainWindow.txtHeroesName.toPlainText():
            Echo('**ERROR** Heroes Name cannot include a space', Status)
            return False  # Incomplete

        if not len(MainWindow.txtHeroesFancyName.toPlainText()):
            Echo('**MISSING** Heroes Fancy Name', Status)
            return False  # Incomplete

        if not len(MainWindow.txtPowers.toPlainText()):
            Echo('**MISSING** List of Powers', Status)
            return False  # Incomplete

        if not len(MainWindow.txtBuffs.toPlainText()):
            Echo('**MISSING** List of Buff Effects', Status)
            return False  # Incomplete

        return True # Everything is Completed

    def Run(self):

        self.MainWindow.show() # Show the Main Window
        self.MainApp.exec_() # Run the GUI Framework

if __name__ == '__main__':

    HeroBuddy = Application() # Initialize the application
    HeroBuddy.Run() # Run the application