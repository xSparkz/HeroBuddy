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

import mechanize # Used for setting up a browser to access websites on the internet
import cookielib # Used to store cookies and session information
import re # Used to execute regular expressions
from common import *

class WWWConnection():

    def __init__(self):

        # Browser
        self.__Browser = mechanize.Browser() # Create an internet browser

        # Cookie Jar
        # Needed to handle sessions
        self.__CookieJar = cookielib.LWPCookieJar()
        self.__Browser.set_cookiejar(self.__CookieJar)

        # Browser Options
        self.__Browser.set_handle_equiv(True)
        self.__Browser.set_handle_redirect(True)
        self.__Browser.set_handle_referer(True)
        self.__Browser.set_handle_robots(False)
        self.__Browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) # For redirects

        # Setup Headers to appear like a regular browser. Without this step the browser may be confused as a BOT and denied service from a website
        self.__Browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        # Gui Connections
        self.__GuiOutput = None #Holds the pointer to a Textbox to output text to the gui when something happens

    def __GetPageSource(self, WebsiteURL):

        # Connect to website
        Echo('Connecting to ' + WebsiteURL, self.__GuiOutput)
        self.__Browser.open(WebsiteURL)

        # Check response
        Response = self.__Browser.response()
        ResponseCode = Response.code

        # Make sure response is good
        if not ResponseCode == 200:  # Look for an 'OK' code (200)

            Echo('Uh Oh! Not sure what happened.. Hmmm...', GuiOutput=self.__GuiOutput)
            Echo('\t- Received response: ' + ResponseCode + ' from server', GuiOutput=self.__GuiOutput)
            Echo('\t - ERROR!!', GuiOutput=self.__GuiOutput)

            raise Exception('Unable to connect to website. Unknown error. Maybe you did something wrong.')  # No point going any further

        # Store page source
        PageSource = Response.read()

        return PageSource

    def ConnectGUI(self, GuiOutput):

        self.__GuiOutput = GuiOutput

    def GetUUID(self, PlayerName):

        # Generate the URL
        WebsiteURL = str(URL_UUID + PlayerName)

        # Get website
        PageSource = self.__GetPageSource(WebsiteURL)

        Echo('Extracting UUID', GuiOutput=self.__GuiOutput)

        Matches = re.findall(REGEX_UUID, PageSource)  # Find the User ID

        if len(Matches) >= 1:
            self.__UserID = Matches[1]  # Second match First one has hyphens
            Echo('Found UUID for (' + PlayerName + '): ' + self.__UserID, GuiOutput=self.__GuiOutput)

            return self.__UserID

        else:

            raise Exception('Unable to read UUID from website. Unexpected format. Parsing error') # Something went wrong

    def GetHeroPermissions(self):

        # Get website
        PageSource = self.__GetPageSource(URL_HERO_PERMISSIONS)

        Echo('Reading Hero Permissions', GuiOutput=self.__GuiOutput)

        IsPermission = False # Track whether or not we are looking at a permission or some un-related line
        Permissions = [] # Create a new list to keep track of the permissions

        for Line in str(PageSource).split("\n"):

            if IsPermission:

                if '- ' in Line: # Assume we found a permission based on the formatting of the permissions file

                    Permission = str(Line).strip() # Remove spaces at beginning and end of line
                    Permission = str(Permission).strip('- ') # Remove hyphens

                    if Permission not in Permissions: # Check to see if the permission is already in our list of permissions

                        Permissions.append(Permission) # Add the permission to the list of permissions

                    continue # Jump back to beginning of for loop and check for next permission

                else:

                    IsPermission = False # We are no longer looking at a permission because theres no hyphen in the line

            if 'permissions:' in Line: IsPermission = True # Found the permissions identifier, should mean that the next line will be a permission

        Permissions.sort() # Sort the permissions into alphabetical order

        Echo('Done!', GuiOutput=self.__GuiOutput)

        return Permissions # Puff puff pass

    def GetSignature(self, uuid):

        # Generate the URL by inserting the uuid
        WebsiteURL = str(URL_SIGNATURE).replace(URL_SIGNATURE_REPLACE_TAG, uuid)

        # Get website
        PageSource = self.__GetPageSource(WebsiteURL)

        Echo('Parsing Texture Information', GuiOutput=self.__GuiOutput)

        Signature = None # Placeholder for Signature
        Value = None # Placeholder for Value

        Matches = re.findall(REGEX_SIGNATURE, PageSource)  # Find the Signature

        if len(Matches) == 1:

            Signature = Matches[0]  # Signature
            Echo('Found Signature', GuiOutput=self.__GuiOutput)

        else:

            raise Exception('Error: Unexpected result. Page format changed?')

        Matches = re.findall(REGEX_VALUE, PageSource)  # Find the Value

        if len(Matches) == 1:

            Value = Matches[0]  # Value
            Echo('Found Value', GuiOutput=self.__GuiOutput)

            return Signature, Value # Return both

        else:

            raise Exception ('Error: Unexpected result. Page format changed?')




