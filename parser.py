import json
import requests
from DateJS import DateJS
import datetime
import time


def getTime(str):
    time = ''
    comma = False
    for x in str:
        if x == ',':
            comma = True
            continue
        if comma:
            time += x
    return time[1:]


def getHour(time):
    return time[:2]


def getMinute(time):
    return time[3:5]


def getSecond(time):
    return time[6:8]

#
# dateStr = '5/21/2019, 11:49:07'
# timer = getTime(dateStr)
# print(timer)
curDate = datetime.datetime.now()
print(curDate.ctime())
date3 = curDate.ctime()
newdate3 = time.strptime(date3,"%a %b %d %H:%M:%S %Y")

# print(curDate.hour)
# print(curDate.minute)
# print(type(curDate.minute))
# print(curDate.second)

#NOW we test how to compare dates!....
date1 = "5/21/2019, 14:00:00"
date2 = "5/21/2019, 14:00:01"

newdate1 = time.strptime(date1,"%m/%d/%Y, %H:%M:%S")
newdate2 = time.strptime(date2,"%m/%d/%Y, %H:%M:%S")

print(newdate1<newdate3)