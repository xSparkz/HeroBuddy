import datetime

# Formats
FORMAT_TIME = '%I:%M (%S) %p' #ex: 12:34 (04) PM
FORMAT_DATE = '%d %b %Y - %A' #ex: 13 Nov 2014 - Monday

# URL's
URL_UUID = 'https://namemc.com/profile/'
URL_SIGNATURE = 'https://sessionserver.mojang.com/session/minecraft/profile/<uuid>?unsigned=false'
URL_SIGNATURE_REPLACE_TAG = '<uuid>'
URL_HERO_PERMISSIONS =  'https://raw.githubusercontent.com/malonnnn/ServerConfig/master/PermissionsEx/permissions.yml'

# File locations
FILE_EFFECTS = 'includes/effects.txt'
FILE_BLOCKS_AND_ITEMS = 'includes/blocks_and_items.txt'
FILE_ENCHANTMENTS = 'includes/enchantments.txt'
FILE_TRAILS = 'includes/trails.txt'


# Date / Time Functions
def TimeStamp(): return datetime.datetime.now().strftime(FORMAT_TIME)
def DateStamp(): return datetime.datetime.now().strftime(FORMAT_DATE)

# Echo function (Print msg to console with timestamp)
def Echo(LineToEcho):

    Line = str(TimeStamp() + '-\t' + LineToEcho) #Format the line with a timestamp
    print Line #Print the line to console
