#15、编写装饰器，为函数加上统计时间的功能
#装饰器用于统计程序的运行时间：
import time
def run_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('the function running use time is %s:秒' %(end_time - start_time))  #输出运行时间
        return res
    return wrapper
#定义函数，并使用装饰器
@run_time
def get_dir_size(filename):
    for i in range(1,100000):
        a = i * i
    print('hello,nihao %s' %filename)
get_dir_size('./data3/tst1.txt')
get_dir_size('./data3/tst1.txt')