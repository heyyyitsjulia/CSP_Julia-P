# Julia Properz, time of day pythyon

import datetime

currenttime = datetime.datetime.now()

print(currenttime.hour)

if currenttime.hour <= 12:
    print ("Good morning!")
elif currenttime.hour <= 18:
    print("Good afternoon!")
else:
    print("Good evening!")