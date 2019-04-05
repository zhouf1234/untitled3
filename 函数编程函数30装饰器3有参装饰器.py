#有参修饰符
#定义装饰器
def auth(driver='file'):        #driver是个默认参数，有默认值'file',即该装饰器是有参装饰器
    def auth2(func):
        def inner(*args, **kwargs):
            #获取用户的输入
            name=input('用户名：')
            pwd=input('密码：')

            if driver == 'file':
                if(name !='admin' or pwd !='123456'):
                    print('用户名或密码错误')
                    return False
            elif driver == 'db':
                pass
            res = func()
            return res
        return inner
    return auth2

#定义函数，并使用装饰器
@auth('file')
#@auth('db')                   #若换@auth('db'),则无论输入什么都返回：你好
def demo():
    return '你好'             #print('你好')也可的
print(demo())