#时间加减
from datetime import datetime,timedelta

#获取当前时间的datetime对象
dt = datetime.now()
print(dt)

#十天之后的时间
dt2 = dt + timedelta(days=10)
print(dt2)

#二十天之前
dt3 = dt + timedelta(days=-20)
print(dt3)

dt4 = dt - timedelta(days=20)
print(dt4)
print()

#十分钟之后
dt5 = dt + timedelta(minutes=10)
print(dt5)

#一天十八小时四十分钟之后；尽量不要加年，不准确
dt6 = dt + timedelta(days=1,hours=18,minutes=40)
print(dt6)
