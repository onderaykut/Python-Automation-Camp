import datetime
from datetime import date, timedelta,time

bugun= date.today()
print('bugunun tarihi',bugun)

dun=bugun+timedelta(days=-1)
print('dunun tarihi', dun)
print(bugun-dun)

yarin=bugun+timedelta(days=1)
print('yarının tarihi',yarin)

print(date.isocalendar(bugun))  #hafta
print(date.weekday(bugun))  #haftanın kacıncı gunu
print(date.ctime(bugun))

zaman= time (15,35)
print(zaman)
dt=datetime.datetime(2025,4,7,15,39,30)
print(dt)

import time
print(time.time())