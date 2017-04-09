import datetime

# Formats
FORMAT_TIME = '%I:%M (%S) %p' #ex: 12:34 (04) PM
FORMAT_DATE = '%d %b %Y - %A' #ex: 13 Nov 2014 - Monday

# Bukkit Color Codes
COLOR_1 = '&1' # Dark Blue
COLOR_2 = '&9' # Blue
COLOR_3 = '&3' # Dark Aqua
COLOR_4 = '&b' # Aqua
COLOR_5 = '&4' # Dark Red
COLOR_6 = '&c' # Red
COLOR_7 = '&e' # Yellow
COLOR_8 = '&6' # Gold
COLOR_9 = '&2' # Dark Green
COLOR_10 = '&a' # Green
COLOR_11 = '&5' # Dark Purple
COLOR_12 = '&d' # Light Purple
COLOR_13 = '&f' # White
COLOR_14 = '&7' # Gray
COLOR_15 = '&8' # Dark Gray
COLOR_16 = '&0' # Black
COLOR_17 = '&k' # Obfuscation
COLOR_18 = '&l' # Bold
COLOR_19 = '&m' # Strikethrough
COLOR_20 = '&n' # Underline
COLOR_21 = '&o' # Italic
COLOR_22 = '&r' # Reset

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
FILE_EXAMPLE_BUFFS = 'includes/example_buffs.txt'
FILE_EXAMPLE_POWERS = 'includes/example_powers.txt'
FILE_TEMPLATE_PERMISSIONS = 'templates/permissions.yml'
FILE_TEMPLATE_HERO = 'templates/hero.ms'
FILE_TEMPLATE_TEMPLATES = 'templates/templates.yml'

# Build files & folders
BUILD_FOLDER_HEROFILE = 'ServerConfig/CommandHelper/LocalPackages/commands/buffs'
BUILD_FOLDER_TEMPLATES = 'ServerConfig/Citizens'
BUILD_FOLDER_PERMISSIONS = 'ServerConfig/PermissionsEx'
BUILD_FILE_TEMPLATES = 'ServerConfig/Citizens/templates.yml'
BUILD_FILE_PERMISSIONS = 'ServerConfig/PermissionsEx/permissions.yml'

# Tabs
TAB_PERMISSIONS = '        ' # Correct spaces for each line
TAB_POWERS = '                ' # Correct spaces for each line

# Arrays
ARRAY_TEMPLATE_SINGLE = '\"<item>\"'
ARRAY_TEMPLATE_MULTIPLE = '\"<item>\",'


# Date / Time Functions
def TimeStamp(): return datetime.datetime.now().strftime(FORMAT_TIME)
def DateStamp(): return datetime.datetime.now().strftime(FORMAT_DATE)

# Echo function (Print msg to console with timestamp)
def Echo(LineToEcho, GuiOutput=None):

    Line = str(TimeStamp() + '- ' + LineToEcho) # Format the line with a timestamp
    print Line # Print the line to console

    if GuiOutput is not None:

        GuiOutput.addItem(Line) # Add the line to the GUI
        GuiOutput.scrollToBottom() # Scroll the list to the bottom
