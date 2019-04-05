#各种形式时间的转换
import time

#输出结构化时间，时间元组，指定时间戳得到结构化时间
print(time.localtime())
print(time.localtime(1539240646.243377))  #1539240646.243377：一个时间戳
print(time.localtime(0))
print(time.gmtime(0))
print()

#格式化时间 转为 结构化时间
data_str ='1999-01-01 12:12:40'
print(time.strptime(data_str,'%Y-%m-%d %X'))
print()

#结构化时间转为格式化时间
print(time.strftime('%Y-%m-%d %X',time.localtime(1539240646.243377)))
print(time.asctime())
print(time.ctime(1539240646.243377))
print()

#结构化时间 转为 时间戳
date_str = '1999-01-01 12:22:23'  # 变为时间戳
print(time.mktime(time.strptime(date_str, '%Y-%m-%d %X')))
