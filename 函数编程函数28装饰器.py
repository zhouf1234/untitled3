import time
#print(time.time()) #时间戳

#定义函数
#def get_dir_size():
    #start_time = time.time()
    #for i in range(1,100000):
        #a = i * i
    #end_time = time.time()
    #print(end_time - start_time)
#get_dir_size()

#装饰器(decorator)就是闭包函数的一种应用场景
#定义装饰器
def run_time(func):
    def wrapper():
        func()
        # pass
    return wrapper
#定义函数，并使用装饰器
@run_time        #@run_time即为装饰器装饰了下方
def get_dir_size():
    for i in range(1,100000):
        a = i * i
    print('hello,nihao')
get_dir_size()
print()

#定义装饰器
#装饰器用于统计程序的运行时间：
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