import calendar
import datetime
month,day,year=list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
