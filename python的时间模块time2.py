#导入模块，格式化时间字符串
#时间日期格式化的符号
import time
print(time.strftime('%Y'))      #当前的日期：年
print(time.strftime('%m'))       #月
print(time.strftime('%d'))        #日
print(time.strftime('%H'))        #当前的时间：时
print(time.strftime('%M'))        #分
print(time.strftime('%S'))         #秒
print(time.strftime('%m/%d/%Y %I'))

print(time.strftime('%p'))         #当前的上午还是下午

print(time.strftime('%j'))         #当前是年内第..天
print()
print(time.strftime('%y'))

print(time.strftime('%a'))
print(time.strftime('%A'))

print(time.strftime('%c'))
print(time.strftime('%x %X'))
print(time.strftime('%Y-%m-%d %X'))

print(time.strftime('%z'))

print(time.strftime('%Y%%'))

