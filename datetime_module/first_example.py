import datetime # standard library

import pytz # recommended even by the standard timezone library

d = datetime.date(2021, 12, 27)
tday = datetime.date.today()
print(tday.weekday())

# timedelta: Difference between 2 dates
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(1993, 12, 11)

tillbday = tday - bday
print(tillbday)

t = datetime.time(9, 30, 45, 10000)
print(t.hour)

# most general to access date and time together
dt = datetime.datetime(2021, 12, 27, 9, 30, 45, 10000)
print(dt.date())
print(dt.time())
print(dt.year)

print(dt + tdelta)

# working with different timezone

dt_today =  datetime.datetime.today() # procide local date info
dt_now = datetime.datetime.now()  # can give timezone info
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt_utc = datetime.datetime(2021, 12, 27, 9, 30, 45, tzinfo=pytz.UTC)

print(dt_utc)

dt_now_utc = datetime.datetime.now(tz=pytz.UTC)
print(dt_now_utc)

dt_myplace = dt_now_utc.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_myplace)


for tz in pytz.all_timezones:
    print(tz)
