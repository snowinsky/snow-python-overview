from datetime import datetime as dt, date as d, time as t
from datetime import timedelta

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(dt.now())
print(d.today())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(d(2011,11,13))
print(dt(2021,12,15,13,11,46,325))
print(t(13,15,18,165))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(d.today().strftime('%Y--%m--%d'))
print(dt.strptime("2022/06/17 15:30:45 PM", "%Y/%m/%d %H:%M:%S %p")) #12小时用I表示时，24小时用H表示时 另外有PM了，就得用12小时，注意时间的一致性
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(d.today() + timedelta(days=-1)) #timedelta是一个时间间隔类
print(timedelta(seconds=120).total_seconds())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
