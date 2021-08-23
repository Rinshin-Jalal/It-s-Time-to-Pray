#!/usr/bin/env python
from prayertimes import PrayTimes
import datetime
import os
import time as t

print("Time to Pray is Running")

today = datetime.date.today()

def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]
 
PT = PrayTimes('Karachi')

times = PT.get_times(today, (11.1216, 76.3435), +5.5)

del times['imsak']
del times['sunrise']
del times['sunset']
del times['midnight']

while True:
    now = datetime.time.strftime(datetime.datetime.now().time(), '%H:%M')
    for key, value in times.items():
        time = datetime.datetime.strptime( f"{today}-{value}", '%Y-%m-%d-%H:%M ')
        prayertime = datetime.datetime.strftime(time,'%H:%M')
        restTime = datetime.datetime.strftime(time + datetime.timedelta(minutes=15), '%H:%M')
        if now is prayertime: 
            # change to your Directory
            os.system("firefox ~/Dev/automation/TimetoPray/prayertime1.html")
            os.system('systemctl poweroff') 
            # os.system('shutdown -force) Windows        
        elif is_between(now,(prayertime,restTime)):
            # change to your Directory
            os.system("firefox ~/Dev/automation/TimetoPray/prayertime2.html")
            os.system('systemctl poweroff') 
            # os.system('shutdown -force') Windows



