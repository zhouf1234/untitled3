#17、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

#定义装饰器
def auth(driver='file'):        #driver是个默认参数，有默认值'file',即该装饰器是有参装饰器
    def auth2(func):
        def inner(*args, **kwargs):
            #获取用户的输入
            name=input('用户名：')
            pwd=input('密码：')
            with open('file-four.txt', 'r') as f:
                data = f.read()
            if driver == 'file':
                if(name not in data or pwd not in data):
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
def demo():
    return '你好'
print(demo())

@auth('db')        #一个装饰器两个函数使用，一个认证成功后，后面的函数不再输出。。。怎么使用
def deo():
    return '输入错误，请重新登录'
print(deo())
