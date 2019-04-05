#18、编写装饰器，为多个函数加上认证功能，
# 要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

#定义装饰器
import time
def auth(driver='file'):
    def auth2(func):
        def inner(*args, **kwargs):
            #获取用户的输入
            name=input('用户名：')
            pwd=input('密码：')

            if driver == 'file':
                if(name !='admin' or pwd !='123456'):
                    print('用户名或密码错误')
                    return False
            start_time = time.time()      #获取程序运行时间；如何指定超时时间？
            res = func(*args, **kwargs)
            end_time = time.time()
            print('the function running use time is %s:秒' % (end_time - start_time))
            return res
        return inner
    return auth2

#定义函数，并使用装饰器
@auth('file')
def demo():
    for i in range(1,100000):          #运行时间的小数点，如果小于四位，则没法显示
        a = i * i
    return '你好'
print(demo())