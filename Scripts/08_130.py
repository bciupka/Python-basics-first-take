import time

print(time.time())

print(time.localtime(time.time()))

import calendar

print(calendar.month(2021, 9, w=3, l=2))

calendar.setfirstweekday(6)

print(calendar.month(2021, 9))

print(calendar.isleap(2000))

print(calendar.monthcalendar(2019, 9))

print(calendar.calendar(2019))
