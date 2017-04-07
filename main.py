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

class HeroBuddyGui(QtGui.QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(HeroBuddyGui, self).__init__(parent)
        self.setupUi(self)

class Application():

    def __init__(self):

        self.MainApp = QtGui.QApplication(sys.argv) # Setup main application
        self.MainWindow = HeroBuddyGui() # Setup main window

        self.Website = webcrawler.WWWConnection()

        # Variables
        self.UUID = ''
        self.Signature = ''
        self.Value = ''

        # Populate Text Boxes
        # (1) Available Permissions
        HeroPermissions = self.Website.GetHeroPermissions()
        self.__CopyListToListView(HeroPermissions, self.MainWindow.listPermissions)

        # (2) Effects
        self.__CopyFileToText(FILE_EFFECTS, self.MainWindow.txtEffects)

        # (3) Blocks and Items
        self.__CopyFileToText(FILE_BLOCKS_AND_ITEMS, self.MainWindow.txtBlocks)

        # (4) Enchantments
        self.__CopyFileToText(FILE_ENCHANTMENTS, self.MainWindow.txtEnchantments)

        # (5) Trails
        self.__CopyFileToListView(FILE_TRAILS, self.MainWindow.listTrails)

        # Setup bindings
        # Connect buttons to Callback Functions
        self.MainWindow.btnCloneToHeroName.mouseReleaseEvent = self.ButtonClick_CloneToHeroName
        self.MainWindow.btnCloneToHeroesSpeech.mouseReleaseEvent = self.ButtonClick_ClonetToHeroSpeech
        self.MainWindow.btnClearScratchPad.mouseReleaseEvent = self.ButtonClick_ClearScratchPad
        self.MainWindow.btnUsePlayerName.mouseReleaseEvent = self.ButtonClick_UsePlayerName

    def ButtonClick_UsePlayerName(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnUsePlayerName)
        self.__CopyTxtToTxt(self.MainWindow.txtPlayerName, self.MainWindow.txtInfoPlayerName)
        self.UUID = self.Website.GetUUID(str(self.MainWindow.txtPlayerName.toPlainText()))
        self.Signature, self.Value = self.Website.GetSignature(self.UUID)

        self.MainWindow.txtInfoUUID.setPlainText(self.UUID)
        self.MainWindow.txtInfoSignature.setPlainText(self.Signature)
        self.MainWindow.txtInfoValue.setPlainText(self.Value)

    def ButtonClick_CloneToHeroName(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnCloneToHeroName)
        self.__CopyTxtToTxt(self.MainWindow.txtScratchPad, self.MainWindow.txtHeroesFancyName)


    def ButtonClick_ClonetToHeroSpeech(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnCloneToHeroesSpeech)
        self.__CopyTxtToTxt(self.MainWindow.txtScratchPad,  self.MainWindow.txtSpeech)

    def ButtonClick_ClearScratchPad(self, MouseEvent):

        self.__ResetButton(self.MainWindow.btnClearScratchPad)
        self.MainWindow.txtScratchPad.clear()

    def __ResetButton(self, Button):
        # Function used to reset a button for a smooth 'click' animation.
        # Seems to hang on Mouse release if callback function is called
        # This function makes it appear seamless

        Button.clearFocus()
        Button.setFocus()

    def __CopyTxtToTxt(self, Source, Destination):
        # Take the text from a Source Textbox and Copy it to the Destination Textbox
        # Cuts down on code

        Destination.clear()
        Destination.appendPlainText(Source.toPlainText())

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

        File = open(FileName, "r") # Open file for reading

        for Line in str(File.read()).split("\n"): # Split the file into Lines using the newline character and read it Line by Line
            TextBox.appendPlainText(Line) # Add the line to the Textbox

        TextBox.moveCursor(QtGui.QTextCursor.Start)  #M ove the cursor to the top of the textbox
        TextBox.ensureCursorVisible()  # Scroll to cursor

        File.close()

    def __CopyFileToListView(self, FileName, ListView):
        # Take a filename and copy the contents of the file to a ListView

        File = open(FileName, "r")  # Open file for reading

        for Line in str(File.read()).split("\n"):  # Split the file into Lines using the newline character and read it Line by Line
            ListView.addItem(Line)  # Add the line to the ListView

        ListView.scrollToTop() # Scroll the list to the top

        File.close()

    def Run(self):

        self.MainWindow.show()
        self.MainApp.exec_()




if __name__ == '__main__':

    HeroBuddy = Application()
    HeroBuddy.Run()
