import time            #获取时间戳time的模块
def run_time(func):    #装饰器1
    '''
    统计函数的运行时间
    '''
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('the function running use time is %s:秒' %(end_time - start_time))  #输出运行时间
        return res
    return wrapper
def log(func):       #装饰器2
    '''
    函数的运行日记
    '''
    def wrapper(*args,**kwargs):
        res = func(*args, **kwargs)
        with open('func_log.txt','a',encoding='gbk')as f:
            f.write('%s函数被调用%s \n' %(func.__name__,time.time()))
        return res
    return wrapper

@run_time
@log                   #两个装饰器
def add(a,b):
    for i in range(1,1000):
        a += 1
        b += 1
    return a + b

print(add(1,2))