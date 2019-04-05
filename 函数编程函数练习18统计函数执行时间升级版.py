#23 装饰器，统计函数执行时间，
# 记录到日志中，执行一次，产生新的日志文件，
# 文件名以日期为名，两次函数执行在同一秒，记录到一个日志中

#两个装饰器，一个统计执行时间，一个写入日志，可以写成一个吗？
#如何才能执行一次产生一个新的日志文件？
#如何获取当前日期的格式为20180926？如何与产生新文件同时执行文件命名？

import time
def run_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func()
        end_time = time.time()
        #计算执行时间：
        runtime=end_time - start_time
        #文件操作，写入文件
        filename='./data3/'+time.strftime('%Y-%m-%d %H %M %S')+'.txt'
        with open(filename,'a',encoding='utf-8')as f:
            msg=func.__name__+'函数被执行时间为'+str(runtime)+'\n'
            f.write(msg)
        return res
    return wrapper
#定义函数，并使用装饰器
@run_time
def fn():
    print('nihao')
@run_time
def demo():
    print('ok!')

fn()
demo()

#print(time.strftime('%Y-%m-%d %H:%M:%S'))