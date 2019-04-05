#定义一个命名关键字参数
#限制关键字参数的名字，就可以用命名关键字参数:此次是username，pwd
#name普通参数，age默认参数
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#如果没有可变参数，就必须加一个*作为特殊分隔符。
def demo_fn(name, age=10, *, username, pwd='12333'):
    print(name,age,username,pwd)
#调用
demo_fn('xiaoli',16,username='admin',pwd='12345')
demo_fn('lili',username='users',pwd='12345')
demo_fn('xiaoli',username='admin')
print()

# 函数 当只有命名关键字参数,前面有*号
def demo_fn01(*, name, age):
    print(name, age)

demo_fn01(name='admin', age=19)
