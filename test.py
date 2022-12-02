import operator
import sys
import urllib3
import json
import time
import re
import subprocess
import datetime
import requests
from requests.exceptions import HTTPError

# Returns the current date and time formated into [Year]-[Month]-[Day]T[Hour]:[Minute]:[Second]
def get_datetime(timestr):
    return datetime.datetime.strptime(timestr[:-5], "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(hours=-5)
# Gets the number the represents the day of the week (i.e. 0 = Sunday, 1 = Monday, ... , 6 = Saturday)
def get_day_of_week(timestr):
    return get_datetime(timestr).isoweekday() % 7


# Requests the schedule for shows from spinitron
http = urllib3.PoolManager()
r = http.request('GET', 'https://spinitron.com/api/spins?access-token=ARdWnef9Fie7lKWspQzn5efv&count=5')



# Loads the json data from the response
data = json.loads(str(r))
# Gets the results from the requests (i.e. All the shows data, start end times etc)
results = data["items"]

spins = [] 
epoch = datetime.datetime(1970, 1, 1)
# Loops through each item in results (the shows)
# For each show, gets the name, id, start time, end time, and duration
# Adds that data to the shows array
for song in results:
    asong = {}
    asong['name'] = song["title"]
    asong["id"] = song["id"]
    asong["offAir"] = song["end"]
    asong["onAir"] = song["start"]
    starttime = get_datetime( asong['onAir'])
    endtime = get_datetime( asong['offAir'])
    asong['onAirDatetime'] = starttime
    asong["starth"] = starttime.hour
    asong["startm"] = starttime.minute
    asong["timestamp"] = int((endtime - epoch).total_seconds())
    asong["totaltime"] = song['duration']
    spins.append( asong)
    print("Added show {}".format( asong['name'].encode('utf-8')))
