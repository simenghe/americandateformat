import json
import requests
from DateJS import DateJS
class nycParse:
    def getTime(str):
        time = ''
        comma = False
        for x in str:
            if x == ',':
                comma = True
                continue
            if comma:
                time += x
        return time.strip()

    def getHour(time):
        return time[:2]

    def getMinute(time):
        return time[3:5]

    def getSecond(time):
        return time[6:8]

# dateStr = '5/21/2019, 11:49:07'
#
# timer = nycParse.getTime(dateStr)
# print(timer)
# curHour =  nycParse.getHour(timer)
# print(curHour)
# curMinute = nycParse.getMinute(timer)
# print(curMinute)
# curSecond = nycParse.getSecond(timer)
# print(curSecond)









