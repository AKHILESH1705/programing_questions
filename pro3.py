from datetime import datetime
import pytz

print(datetime.now())

# only time 
#print(datetime.time(datetime.now()))

# only date 
#print(datetime.date(datetime.now()))


# another way to print date and time
#import datetime as dt
#now = dt.datetime.now()
#print ("Current date and time : ")
#print(now) # it will give  time like 14:25:40.26598
#print (now.strftime("%Y-%m-%d %H:%M:%S"))# these statement gives  accurate time like 14:25:40  
