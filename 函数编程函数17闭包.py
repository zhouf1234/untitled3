# 闭包
# 闭包形成的条件：必须有嵌套函数，嵌套必须引用外层作用域的变量,外层函数返回内嵌函数
#闭包：即为创建函数的函数，每调用一个，就返回一个新的函数；即下方例子的res 和c1，c2, c3
def fn_wrapper():
    num = 100
    def fn_inner():
        print(num)
    return fn_inner
res = fn_wrapper()          #res即为闭包函数
res()       #内层有print，也只有一个num，所以此处不可写成print(res())，否则返回100和none两行
res()         #显示100
print()


def make_counter():
    num = 1
    def counter():
        nonlocal num   #声明该变量是上层作用域的变量
        num += 1        #上方不写nonlocal，此处报错
        return num
    return counter
#调用
c1 = make_counter()
c2 = make_counter()
c3 = make_counter()
print(c1())        #输出一次递加一个2
print(c1())        #3
print(c1())        #4
print(c2())        #2
print(c2())        #3
print(c3())        #2
