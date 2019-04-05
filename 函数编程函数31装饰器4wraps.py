import time            #获取时间戳time的模块
from functools import wraps
def log(func):
    '''
    函数的运行日记
    '''

    @wraps(func)
    def wrapper(*args,**kwargs):
        """
              我是wrapper
              """
        res = func(*args, **kwargs)
        with open('func_log.txt','a',encoding='gbk')as f:
            f.write('%s函数被调用%s \n' %(func.__name__,time.time()))
        return res
    return wrapper
@log
def add(a,b):
    """
        a和b的和
    """
    return a+b
print(add.__name__) #函数名
print(add.__doc__) #注释
