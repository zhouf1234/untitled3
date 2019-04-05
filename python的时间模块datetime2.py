#其他形式的时间 转为 datetime对象(时间戳，字符串)
from datetime import datetime

#datetime.fromtimestamp(时间戳)返回datetime对象，通过时间戳指定时间
dt = datetime.fromtimestamp(11112222)
print(dt)
print()
#字符串返回datetime对象，通过字符串指定时间
dt = datetime.strptime('12/23/2020 23:12:23', '%m/%d/%Y %X')
print(dt)