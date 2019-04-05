#import datetime
from datetime import datetime

#获取当前时间
#print(datetime.datetime.now())   #与import datetime对应
print(datetime.now())
#获取标准时区时间
print(datetime.utcnow())
print()

dt = datetime.now()
print(dt)  #获取当前时间
print()

dt = datetime(2028,12,4)
dt = datetime(2028, 12, 4, 12, 23)
dt = datetime(2028,12,4,12,23,56)
print(dt)  #获取指定的日期时间:最好三个参数年 月 日，最多七个
print()

print(dt.timestamp())   #datetime类型 转 时间戳，此处是dt
print(dt.strftime('%m/%d/%Y %X'))
