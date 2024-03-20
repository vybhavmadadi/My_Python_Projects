#Date Time Import Tutorial
import datetime

#Naive datetimes - Don't have information to determine timezones and DST times. Good to work if this info is not needed
#Aware datetimes - Opposite of Naive date times

# # Naive datetimes:

# d = datetime.date(2016, 7, 24) #Format of date is YYYY, M, DD
# tday = datetime.date.today() # Get today's date
# # print(d)
# # print(tday) # Get full date
# # print(tday.year) # Further drill down possible from this variable of date
# # print(tday.weekday()) # Gets weekday where Monday is 0 thru to Sunday is 6
# # print(tday.isoweekday()) # Gets ISO weekday where Monday is 1 thru to Sunday is 7

# #Time Delta - Define a delta and use in code to add or subtract a time delta from a given date
# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)
# print(tday - tdelta)

# # date2 = date1 + timedelta
# #timedelta = date1 + date2
# bday = datetime.date(2025, 3, 10)

# till_bday = bday - tday #This returns a time delta
# print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds()) #Prints output in seconds

# #TIME DEFINITIONS
# t = datetime.time(9, 30, 45, 100000) #This will be in format hours:mins:seconds:milliseconds
# print(t)
# print(t.hour)

# #FULL DATE TIME DEFINITIONS
# dt = datetime.datetime(2024, 7, 26, 12, 30, 45, 100000) #Format in yyyy, m, dd, hh, mm, ss, ssssss
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)
# print(dt + tdelta)
# tdelta_2 = datetime.timedelta(hours=12) # When you use datetime.datetime, you can define deltas and use them in hours
# print(dt + tdelta_2)

# #Alternative constructors
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.now(datetime.UTC) #This is the new suggeted method as datetime.UTC is deprecated

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

#USING PYTZ Package - Third Party. Install using pip install pytz in terminal
import pytz

# #Recommended to always work with UTC for pytz
# dt = datetime.datetime(2024, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# # #convert this time to my timezone
# # dt_mel = dt_utcnow.astimezone(pytz.timezone('Australia/Melbourne'))
# # print(dt_mel)

# # #Print out all available timezones for pytz
# # for tz in pytz.all_timezones:
# #     print(tz)

# #Converting naive datetime to an aware datetime
# date_naive = datetime.datetime.now() #Naive datetime
# aumel_tz = pytz.timezone('Australia/Melbourne') #Pass pytz timezone to a variable

# date_ausmel = aumel_tz.localize(date_naive) #Use the pytz timezone varaiable to localise the naive time

# print(date_naive)
# print(date_ausmel)

#Different ways to display datetimes
dt_ausmel = datetime.datetime.now(tz=pytz.timezone('Australia/Melbourne'))

print(dt_ausmel.isoformat())
#Look at python docs for codes that the date can be printed out in at 'https://docs.python.org/<<yourpythonversion>>/library/datetime.html'
print(dt_ausmel.strftime('%B %d, %Y'))

#Convert string to datetime
dt_str = 'March 20, 2024'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y') #Convert above string to datetime
print(dt)

#strftime - Datetime to String
#strptime - String to Datetime