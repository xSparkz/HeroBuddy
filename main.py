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

import webcrawler

class Main():

    def Run(self):

        WebSite = webcrawler.WWWConnection()

        uuid = WebSite.GetUUID('xSp4rkz')
        Signature, Value = WebSite.GetSignature(uuid)


if __name__ == "__main__":

    HeroBuddy = Main() #Setup Application
    HeroBuddy.Run() #Run Application