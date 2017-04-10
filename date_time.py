from datetime import datetime, timedelta
import time

# Basic date operation
now = datetime.now()
yesterday = now - timedelta(days=1)
lastYear = datetime(2016,3,8,0,0,0,0) # create a datime object with (year, month, day, hour, minute, seconds, milliseconds)
print(str(now))
print(str(yesterday) + ' ***** \n')

# convert a date string into an datetime object
datestr = "2017-03-07"
date = datetime.strptime(datestr,"%Y-%m-%d")
print(str(date) + ' ***** \n')

def create_file(filename):
    """Create an empty file with datetime as filename"""
    with open(filename.strftime('%Y%m%d_%H-%M-%S.%f') + ".txt","w") as file:
        file.write('')

#create_file(now)

#use of time object
list =[]
for i in range(3):
    list.append(datetime.now())
    time.sleep(1)

for i in list:
    print(i)
