#还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法
# 在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
fn_dict={}
from functools import wraps
def log(func):
    def wrapper(*args,**kwargs):
        if func.__name__ not in fn_dict:
            fn_dict[func.__name__] = func
        res=func()
        return res
    return wrapper

@log
def fn1():
    pass

@log
def fn2():
    print('111')

@log
def fn3():
    pass

fn1()
fn2()
fn3()

print(fn_dict)

