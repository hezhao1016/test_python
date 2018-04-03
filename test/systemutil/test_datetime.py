# datetime | datetime是Python处理日期和时间的标准库。

# 获取当前日期和时间

from datetime import datetime

now = datetime.now()  # 获取当前datetime
print(now)
print(type(now))

# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# datetime.now()返回当前日期和时间，其类型是datetime


# 获取指定日期和时间

from datetime import datetime
dt = datetime(2018, 3, 12, 10, 25, 54)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.date())
print(dt.time())


# datetime转换为timestamp
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
print(dt.timestamp())


# timestamp转换为datetime
t = 1520821554.0
print(datetime.fromtimestamp(t))  # 本地时间 | 转换结果和当前操作系统的时区相关
# timestamp也可以直接被转换到UTC标准时区的时间
print(datetime.utcfromtimestamp(t))  # UTC时间


# str转为datetime
cday = datetime.strptime('2018-03-12 14:21:55', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
datestr1 = now.strftime('%a, %b %d %H:%M')
datestr2 = now.strftime('%Y-%m-%d %H:%M:%S')
print(datestr1)
print(datestr2)


# datetime加减
print('========================')
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


print('========================')
# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
from datetime import datetime, timedelta, timezone
tz_uc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
print('当前时间：', now)
dt = now.replace(tzinfo=tz_uc_8)  # 强制设置为UTC+8:00
# dt1 = datetime(2018, 3, 12, 17, 2, 10, 871012, tzinfo=timezone(timedelta(hours=8)))
print('强制设置为UTC+8:00时间：', dt)

# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC时间：', utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间：', bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时间：', tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时间：', tokyo_dt2)
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。



# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。