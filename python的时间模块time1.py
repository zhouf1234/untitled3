#导入模块
import time
print('时间戳:',time.time())#获取当前时间的时间戳
print('格式化时间字符串：',time.strftime('%Y-%m-%d %H:%M:%S')) #获取当前时间的格式化时间字符串
print('时间元组：',time.localtime()) #获取本地时间的元组
print('时间元组：',time.gmtime())  #获取标准时区的时间