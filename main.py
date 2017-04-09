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

import webcrawler # Functions to interact with internet such as obtaining users UUID or skin information
import sys # Used to supply argv to application
import gui # All of the GUI code independent from functional code
from PyQt4 import QtGui # Library for working with GUI
from common import *
import os # Used to manipulate files and folders

class HeroBuddyGui(QtGui.QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(HeroBuddyGui, self).__init__(parent)
        self.setupUi(self)

class Application():

    def __init__(self):

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
        self.MainWindow.btnCloneToHeroName.mouseReleaseEvent = self.ButtonClick_CloneToHeroName
        self.MainWindow.btnCloneToHeroesSpeech.mouseReleaseEvent = self.ButtonClick_ClonetToHeroSpeech
        self.MainWindow.btnCloneToHeroesChatColor.mouseReleaseEvent = self.ButtonClick_CloneToChatColor
        self.MainWindow.btnClearScratchPad.mouseReleaseEvent = self.ButtonClick_ClearScratchPad
        self.MainWindow.btnUsePlayerName.mouseReleaseEvent = self.ButtonClick_UsePlayerName
        self.MainWindow.btnLoadBuffsExample.mouseReleaseEvent = self.ButtonClick_LoadExampleBuffs
        self.MainWindow.btnLoadPowersExamples.mouseReleaseEvent = self.ButtonClick_LoadExamplePowers
        self.MainWindow.btnCreate.mouseReleaseEvent = self.ButtonClick_Build

        #Bukkit Color Code Buttons
        self.MainWindow.btnColor_1.mouseReleaseEvent = self.ButtonClick_Color_1
        self.MainWindow.btnColor_2.mouseReleaseEvent = self.ButtonClick_Color_2
        self.MainWindow.btnColor_3.mouseReleaseEvent = self.ButtonClick_Color_3
        self.MainWindow.btnColor_4.mouseReleaseEvent = self.ButtonClick_Color_4
        self.MainWindow.btnColor_5.mouseReleaseEvent = self.ButtonClick_Color_5
        self.MainWindow.btnColor_6.mouseReleaseEvent = self.ButtonClick_Color_6
        self.MainWindow.btnColor_7.mouseReleaseEvent = self.ButtonClick_Color_7
        self.MainWindow.btnColor_8.mouseReleaseEvent = self.ButtonClick_Color_8
        self.MainWindow.btnColor_9.mouseReleaseEvent = self.ButtonClick_Color_9
        self.MainWindow.btnColor_10.mouseReleaseEvent = self.ButtonClick_Color_10
        self.MainWindow.btnColor_11.mouseReleaseEvent = self.ButtonClick_Color_11
        self.MainWindow.btnColor_12.mouseReleaseEvent = self.ButtonClick_Color_12
        self.MainWindow.btnColor_13.mouseReleaseEvent = self.ButtonClick_Color_13
        self.MainWindow.btnColor_14.mouseReleaseEvent = self.ButtonClick_Color_14
        self.MainWindow.btnColor_15.mouseReleaseEvent = self.ButtonClick_Color_15
        self.MainWindow.btnColor_16.mouseReleaseEvent = self.ButtonClick_Color_16
        self.MainWindow.btnColor_17.mouseReleaseEvent = self.ButtonClick_Color_17
        self.MainWindow.btnColor_18.mouseReleaseEvent = self.ButtonClick_Color_18
        self.MainWindow.btnColor_19.mouseReleaseEvent = self.ButtonClick_Color_19
        self.MainWindow.btnColor_20.mouseReleaseEvent = self.ButtonClick_Color_20
        self.MainWindow.btnColor_21.mouseReleaseEvent = self.ButtonClick_Color_21
        self.MainWindow.btnColor_22.mouseReleaseEvent = self.ButtonClick_Color_22

    # All Color buttons are responsible for grabbing the corresponding Bukkit Color code
    # and inserting that code into the scratch pad on the Colors tab
    # Helps with building a Heroes Name
    def ButtonClick_Color_1(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_1)
        self.__InsertTxtToTxt(COLOR_1, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_2(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_2)
        self.__InsertTxtToTxt(COLOR_2, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_3(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_3)
        self.__InsertTxtToTxt(COLOR_3, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_4(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_4)
        self.__InsertTxtToTxt(COLOR_4, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_5(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_5)
        self.__InsertTxtToTxt(COLOR_5, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_6(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_6)
        self.__InsertTxtToTxt(COLOR_6, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_7(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_7)
        self.__InsertTxtToTxt(COLOR_7, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_8(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_8)
        self.__InsertTxtToTxt(COLOR_8, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_9(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_9)
        self.__InsertTxtToTxt(COLOR_9, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_10(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_10)
        self.__InsertTxtToTxt(COLOR_10, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_11(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_11)
        self.__InsertTxtToTxt(COLOR_11, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_12(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_12)
        self.__InsertTxtToTxt(COLOR_12, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_13(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_13)
        self.__InsertTxtToTxt(COLOR_13, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_14(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_14)
        self.__InsertTxtToTxt(COLOR_14, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_15(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_15)
        self.__InsertTxtToTxt(COLOR_15, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_16(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_16)
        self.__InsertTxtToTxt(COLOR_16, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_17(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_17)
        self.__InsertTxtToTxt(COLOR_17, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_18(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_18)
        self.__InsertTxtToTxt(COLOR_18, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_19(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_19)
        self.__InsertTxtToTxt(COLOR_19, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_20(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_20)
        self.__InsertTxtToTxt(COLOR_20, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_21(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_21)
        self.__InsertTxtToTxt(COLOR_21, self.MainWindow.txtScratchPad)

    def ButtonClick_Color_22(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnColor_22)
        self.__InsertTxtToTxt(COLOR_22, self.MainWindow.txtScratchPad)

    def ButtonClick_UsePlayerName(self, MouseEvent):
        # Grabs the UUID along with the Texture Signature and Value from Minecraft websites
        # connected to the PlayerName

        self.__ResetButton(self.MainWindow.btnUsePlayerName) # Resets the button from a pressed state to an unpressed state *bug fix*
        self.__CopyTxtToTxt(self.MainWindow.txtPlayerName, self.MainWindow.txtInfoPlayerName) # Copy the PlayerName to the Player Info Tab
        self.UUID = self.Website.GetUUID(str(self.MainWindow.txtPlayerName.toPlainText())) # Grab UUID
        self.Signature, self.Value = self.Website.GetSignature(self.UUID) # Grab the Signature and Value

        self.Signature = str(self.Signature).replace('\n', '').replace('\r', '') # Remove the newlines
        self.Value = str(self.Value).replace('\n', '').replace('\r', '') # Remove the newlines

        self.MainWindow.txtInfoUUID.setPlainText(self.UUID) # Display the UUID
        self.MainWindow.txtInfoSignature.setPlainText(self.Signature) # Display the Signature
        self.MainWindow.txtInfoValue.setPlainText(self.Value) # Display the Value

    def ButtonClick_CloneToHeroName(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnCloneToHeroName)
        self.__CopyTxtToTxt(self.MainWindow.txtScratchPad, self.MainWindow.txtHeroesFancyName)

    def ButtonClick_CloneToChatColor(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnCloneToHeroesChatColor)
        self.__CopyTxtToTxt(self.MainWindow.txtScratchPad, self.MainWindow.txtChatColor)

    def ButtonClick_ClonetToHeroSpeech(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnCloneToHeroesSpeech)
        self.__CopyTxtToTxt(self.MainWindow.txtScratchPad,  self.MainWindow.txtSpeech)

    def ButtonClick_ClearScratchPad(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnClearScratchPad)
        self.MainWindow.txtScratchPad.clear()

    def ButtonClick_LoadExampleBuffs(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnLoadBuffsExample)
        self.__CopyFileToText(FILE_EXAMPLE_BUFFS, self.MainWindow.txtBuffs)

    def ButtonClick_LoadExamplePowers(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnLoadPowersExamples)
        self.__CopyFileToText(FILE_EXAMPLE_POWERS, self.MainWindow.txtPowers)

    def ButtonClick_Build(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnCreate)

        Status = self.MainWindow.listStatus  # Pointer to our status window

        Echo('Creating Hero', Status)
        Echo('Checking for Completion', Status)

        if self.__CheckForCompletion(): # Is everything complete?

            Echo('Good to Go!', Status)

            # Make the heroes name lower case so it can be used to create the files
            self.HeroesName = str(self.MainWindow.txtHeroesName.toPlainText()).lower()

            BuildFolder = str(QtGui.QFileDialog.getExistingDirectory())

            if len(BuildFolder) < 1:
                return # User cancelled or didn't select a folder

            Folders = [] # Create a new list of folders to be created

            Folders.append(BuildFolder + '/' + BUILD_FOLDER_HEROFILE)
            Folders.append(BuildFolder + '/' + BUILD_FOLDER_PERMISSIONS)
            Folders.append(BuildFolder + '/' + BUILD_FOLDER_TEMPLATES)

            for Folder in Folders:

                Echo('Checking if folder exists: ' + Folder, Status)

                if not os.path.exists(Folder):

                    Echo('**CREATE** ' + Folder, Status)
                    os.makedirs(Folder)

            # (1) Permissions File
            Template = open(FILE_TEMPLATE_PERMISSIONS, "r")  # Open file for reading
            File = open(BuildFolder + '/' + BUILD_FILE_PERMISSIONS, 'a') # Open file for writting

            Echo('Creating Permissions.yml file: ', Status)

            for Line in str(Template.read()).split("\n"):  # Split the file into Lines using the newline character and read it Line by Line

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

                    SelectedPermissions = self.MainWindow.listPermissions.selectedItems()
                    Permissions = []

                    for Permission in list(SelectedPermissions):

                        Permissions.append(str(Permission.text()))

                    for Permission in Permissions:

                        File.write(str(TAB_PERMISSIONS + '- ' + Permission) + "\n")

                    if len(self.MainWindow.txtHeroPermissions.toPlainText()) > 1:

                        for Permission in str(self.MainWindow.txtHeroPermissions.toPlainText()).split("\n"):

                            File.write(str(TAB_PERMISSIONS + '- ' + Permission) + "\n")

                    continue

                File.write(Line + "\n")

            File.close()
            Template.close()
            Echo('Done!', Status)

        # (2) Hero File
        Template = open(FILE_TEMPLATE_HERO, "r")  # Open file for reading
        File = open(BuildFolder + '/' + BUILD_FOLDER_HEROFILE + '/' + self.HeroesName + '.ms', 'w')  # Open file for writting

        Echo('Creating Hero.ms file', Status)

        for Line in str(Template.read()).split(
                "\n"):  # Split the file into Lines using the newline character and read it Line by Line

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

                if self.MainWindow.checkBoxOP.isChecked():
                    File.write(str(Line).replace('<op>', 'true') + "\n")
                else:
                    File.write(str(Line).replace('<op>', 'false') + "\n")

                continue

            if '<trail>' in Line:

                SelectedTrails = self.MainWindow.listTrails.selectedItems()
                Trails = []
                TrailLine = ''

                for Trail in list(SelectedTrails):
                    Trails.append(str(Trail.text()))

                for Trail in Trails:
                    TrailLine = TrailLine + Trail + ', '

                File.write(str(Line).replace('<trail>', str(str(TrailLine).strip()).strip(',')) + "\n")

                continue

            if '<powers>' in Line:

                Powers = str(self.MainWindow.txtPowers.toPlainText()).split("\n")
                NumberOfPowers = len(Powers)

                if NumberOfPowers == 1:
                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Powers[0]).strip('\"'))) + "\n")
                    continue

                for index, Power in enumerate(Powers):

                    if index == (NumberOfPowers - 1):
                        File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Power).strip('\"'))) + "\n")
                        continue

                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_MULTIPLE).replace('<item>', str(Power).strip('\"'))) + "\n")


                continue

            if '<buffs>' in Line:

                Buffs = str(self.MainWindow.txtBuffs.toPlainText()).split("\n")
                NumberOfBuffs = len(Buffs)

                if NumberOfBuffs == 1:
                    File.write(str(TAB_POWERS + str(ARRAY_TEMPLATE_SINGLE).replace('<item>', str(Buffs[0]).strip('\"'))) + "\n")
                    continue

                for index, Buff in enumerate(Buffs):

                    if index == (NumberOfBuffs - 1):
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

    def __ResetButton(self, Button):
        # Function used to reset a button for a smooth 'click' animation.
        # Seems to hang on Mouse release if callback function is called
        # This function makes it appear seamless

        Button.clearFocus() # Take away focus to prevent the button animation from 'sticking'
        Button.setFocus() # Return focus to the button after animation as completed *Bug Fix*

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
