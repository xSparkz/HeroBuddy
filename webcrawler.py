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

import mechanize, cookielib, re
from bs4 import BeautifulSoup
from common import Echo

URL_UUID = 'https://namemc.com/profile/'
URL_SIGNATURE = 'https://sessionserver.mojang.com/session/minecraft/profile/<uuid>?unsigned=false'
URL_SIGNATURE_REPLACE_TAG = '<uuid>'
URL_HERO_PERMISSIONS =  'https://raw.githubusercontent.com/malonnnn/ServerConfig/master/PermissionsEx/permissions.yml'

class WWWConnection():

    def __init__(self):

        #Browser
        self.__Browser = mechanize.Browser()

        #Cookie Jar
        self.__CookieJar = cookielib.LWPCookieJar()
        self.__Browser.set_cookiejar(self.__CookieJar)

        #Browser Options
        self.__Browser.set_handle_equiv(True)
        self.__Browser.set_handle_redirect(True)
        self.__Browser.set_handle_referer(True)
        self.__Browser.set_handle_robots(False)

        self.__Browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self.__Browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def __GetPageSource(self, WebsiteURL):

        #Connect to website
        Echo('Connecting to ' + WebsiteURL)
        self.__Browser.open(WebsiteURL)

        #Check response
        Response = self.__Browser.response()
        ResponseCode = Response.code

        #Make sure response is good
        if not ResponseCode == 200:  # Look for an 'OK' code (200)

            Echo('Uh Oh! Not sure what happened.. Hmmm...')
            Echo(('\t- Received response: ' + ResponseCode + ' from server'))
            Echo('\t - ERROR!!')

            raise Exception('Unable to connect to website. Unknown error. Maybe you did something wrong.')  #No point going any further

        # Store page source
        PageSource = Response.read()

        return PageSource


    def GetUUID(self, PlayerName):

        #Generate the URL
        WebsiteURL = str(URL_UUID + PlayerName)

        #Get website
        PageSource = self.__GetPageSource(WebsiteURL)

        Echo('Extracting UUID')

        #Prepare the Website Source Code to be read using BeautifulSoup
        HTML = BeautifulSoup(PageSource)

        #Get UUID
        uuidList = HTML.findAll('span', attrs={'class': 'uuid'})

        #Did we find the UUID's? There should be 2
        if uuidList is not None:

            if len(uuidList) > 1: #Check to see if theres more than 1. There should be 2

                uuid = str(uuidList[1].string.extract()).strip() #Grab the SPAN tag and extract the text in between the html tags
                Echo('Found UUID for (' + PlayerName + '): ' + uuid)
                return uuid

        else:

            raise Exception('Unable to read UUID from website. Unexpected format. Parsing error') #Something went wrong

    def GetHeroPermissions(self):

        #Get website
        PageSource = self.__GetPageSource(URL_HERO_PERMISSIONS)

        Echo('Reading Hero Permissions')

        IsPermission = False #Track whether or not we are looking at a permission or some un-related line
        Permissions = [] #Create a new list to keep track of the permissions

        for Line in str(PageSource).split("\n"):

            if IsPermission:

                if '- ' in Line: #Assume we found a permission based on the formatting of the permissions file

                    Permission = str(Line).strip() #Remove spaces at beginning and end of line
                    Permission = str(Permission).strip('- ') #Remove hyphens

                    if Permission not in Permissions: #Check to see if the permission is already in our list of permissions

                        Permissions.append(Permission) #Add the permission to the list of permissions

                    continue #Jump back to beginning of for loop and check for next permission

                else:

                    IsPermission = False #We are no longer looking at a permission because theres no hyphen in the line

            if 'permissions:' in Line: IsPermission = True #Found the permissions identifier, should mean that the next line will be a permission

        Permissions.sort() #Sort the permissions into alphabetical order

        return Permissions #Puff puff pass

    def GetSignature(self, uuid):

        # Generate the URL by inserting the uuid
        WebsiteURL = str(URL_SIGNATURE).replace(URL_SIGNATURE_REPLACE_TAG, uuid)

        # Get website
        PageSource = self.__GetPageSource(WebsiteURL)

        Echo('Parsing Texture Information')

        #Remove Brackets
        PageSource = str(PageSource).replace('{',"") #{
        PageSource = str(PageSource).replace('}', "") #}
        PageSource = str(PageSource).replace('[', "") #[
        PageSource = str(PageSource).replace(']', "") #]

        #Split the values. Should end up with 5 Values
            #(0) id (uuid)
            #(1) name (name)
            #(2) properties ("signature") (signature)
            #(3) name ("textures")
            #(4) value (value)

        Values = str(PageSource).split(',')

        Signature = '' #Placeholder for extracted signature
        Value = '' #Placeholder for extracted value

        if len(Values) == 5: #We did something right

            Echo('Extracting Signature')
            SubValues = str(Values[2]).split(':')
            Signature = str(SubValues[2]).strip('"')

            Echo('Extracting Value')
            SubValues = str(Values[4]).split(':')
            Value = str(SubValues[1]).strip('"')

            return Signature, Value

        else:
            raise Exception ('Error: Unexpected result. Page format changed?')




