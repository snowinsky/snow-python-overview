#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

print(time.time()) #1712639246.5969875
print(time.localtime(time.time())) #time.struct_time(tm_year=2024, tm_mon=4, tm_mday=9, tm_hour=13, tm_min=7, tm_sec=26, tm_wday=1, tm_yday=100, tm_isdst=0)
print(time.localtime()) #time.struct_time(tm_year=2024, tm_mon=4, tm_mday=9, tm_hour=13, tm_min=7, tm_sec=26, tm_wday=1, tm_yday=100, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #2024-04-09 13:07:26
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) #Tue Apr 09 13:07:26 2024
    # python中时间日期格式化符号：
    #
    # %y 两位数的年份表示（00-99）
    # %Y 四位数的年份表示（000-9999）
    # %m 月份（01-12）
    # %d 月内中的一天（0-31）
    # %H 24小时制小时数（0-23）
    # %I 12小时制小时数（01-12）
    # %M 分钟数（00-59）
    # %S 秒（00-59）
    # %a 本地简化星期名称
    # %A 本地完整星期名称
    # %b 本地简化的月份名称
    # %B 本地完整的月份名称
    # %c 本地相应的日期表示和时间表示
    # %j 年内的一天（001-366）
    # %p 本地A.M.或P.M.的等价符
    # %U 一年中的星期数（00-53）星期天为星期的开始
    # %w 星期（0-6），星期天为星期的开始
    # %W 一年中的星期数（00-53）星期一为星期的开始
    # %x 本地相应的日期表示
    # %X 本地相应的时间表示
    # %Z 当前时区的名称
    # %% %号本身
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))) #1459175064.0

# 1	time.altzone
# 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# 2	time.asctime([tupletime])
# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# 3	time.clock( )
# 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
# 4	time.ctime([secs])
# 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
# 5	time.gmtime([secs])
# 接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
# 6	time.localtime([secs])
# 接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
# 7	time.mktime(tupletime)
# 接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
# 8	time.sleep(secs)
# 推迟调用线程的运行，secs指秒数。
# 9	time.strftime(fmt[,tupletime])
# 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
# 10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
# 根据fmt的格式把一个时间字符串解析为时间元组。
# 11	time.time( )
# 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 12	time.tzset()
# 根据环境变量TZ重新初始化时间相关设置。



import calendar

print(calendar.month(2024,3)) #居然真的输出一个日历，牛逼
#      March 2024
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

# 1	calendar.calendar(year,w=2,l=1,c=6)
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# 2	calendar.firstweekday( )
# 返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。
# 3	calendar.isleap(year)
# 是闰年返回 True，否则为 False。
#
# >>> import calendar
# >>> print(calendar.isleap(2000))
# True
# >>> print(calendar.isleap(1900))
# False
# 4	calendar.leapdays(y1,y2)
# 返回在Y1，Y2两年之间的闰年总数。
# 5	calendar.month(year,month,w=2,l=1)
# 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
# 6	calendar.monthcalendar(year,month)
# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
# 7	calendar.monthrange(year,month)
# 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
# 8	calendar.prcal(year,w=2,l=1,c=6)
# 相当于 print calendar.calendar(year,w=2,l=1,c=6)。
# 9	calendar.prmonth(year,month,w=2,l=1)
# 相当于 print calendar.month(year,month,w=2,l=1) 。
# 10	calendar.setfirstweekday(weekday)
# 设置每周的起始日期码。0（星期一）到6（星期日）。
# 11	calendar.timegm(tupletime)
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
# 12	calendar.weekday(year,month,day)
# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。

import datetime
# datetime 就是对date和time的结合
print(datetime.time)
print(datetime.datetime)
print(datetime.date)
print(datetime.timedelta)
print(datetime.timezone)
print(datetime.tzinfo)
# <class 'datetime.time'>
# <class 'datetime.datetime'>
# <class 'datetime.date'>
# <class 'datetime.timedelta'>
# <class 'datetime.timezone'>
# <class 'datetime.tzinfo'>