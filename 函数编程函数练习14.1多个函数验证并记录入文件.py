def auth(func):
    def wrapper(*args, **kwargs):
        #判断是否已经验证过
        with open('auth-func.txt','r',encoding='utf-8')as f:
            if func.__name__+'\n' not in f.readlines():
                #获取用户的输入
                name = input('用户名：')
                pwd = input('密码：')

                #验证用户输入
                with open('file-auth.txt', 'r', encoding='utf-8')as auth_f:
                    user_dict = eval(auth_f.read())
                if name != user_dict['name'] or pwd != user_dict['pwd']:
                    print('用户名或密码不正确，验证失败')
                    return
                #把验证成功的函数记录下来
                with open('auth-func.txt', 'a', encoding='utf-8')as func_f:
                    func_f.write(func.__name__+'\n')
        res = func()
        return res
    return wrapper

@auth
def fn():
    print('hello')

@auth
def fa():
    print('你好')

fn()
fa()
#第一次成功输入用户名密码后，需要再验证一次，后面再次运行这个这个程序时，因为验证过的函数已经写入文件记录
#再次运行会直接显示验证成功后输出的hello，你好，不用再次登录了
fn()
fa()


