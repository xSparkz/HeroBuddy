import datetime

#Formats
FORMAT_TIME = '%I:%M (%S) %p' #ex: 12:34 (04) PM
FORMAT_DATE = '%d %b %Y - %A' #ex: 13 Nov 2014 - Monday

#Date / Time Functions
def TimeStamp(): return datetime.datetime.now().strftime(FORMAT_TIME)
def DateStamp(): return datetime.datetime.now().strftime(FORMAT_DATE)

#Echo function (Print msg to console with timestamp)
def Echo(LineToEcho):
    print TimeStamp(), '-\t', LineToEcho