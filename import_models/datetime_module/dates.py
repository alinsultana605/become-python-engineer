import datetime
import pytz

# d = datetime.date(2016,7,24)
# tday = datetime.date.today()
# print(tday.year)

# print(tday.weekday())
# print(tday.isoweekday())
# Monday 0 Sunday 6
#for iso Monday 1 Sunday 7

# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

# bday = datetime.date(2026, 6, 28)

# till_bday = bday - tday
# print(till_bday.total_seconds())


# t = datetime.time(9, 30, 45, 100000)
# dt = datetime.datetime(2026, 7, 26, 12, 30, 45, 100000)
# tdelta = datetime.timedelta(hours=12)
# print(dt + tdelta)
# print(dt)
# print(dt.time())
# print(t.hour)

# dt = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt)
# print(dt_now)
# print(dt_utcnow)


# dt = datetime.datetime(2026, 7, 17, 14, 9, 45, tzinfo=pytz.UTC)
# print(dt)
dt_current = datetime.datetime.now()
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)


# for tz in pytz.all_timezones:
#     print(tz)
dt_local = datetime.datetime.now()
print(dt_local)
dt_east = dt_now.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
# print(dt_utcnow)

mtn_tz = pytz.timezone('US/Mountain')
dtm_mtn = mtn_tz.localize(dt_current)
print(dtm_mtn)

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)