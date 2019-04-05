#函数名本质上就是变量名
def demo():
    print('nihao')
    return 1000
print(demo)         #function对象
demo()               #显示nihao
print(demo())        #输出nihao，返回值1000两行
print(type(demo))   #class function
print(type(demo()))  #class int
print()
#函数可以被引用
#函数名就是变量名
#函数可以当作参数传递
#返回值可以是函数
#函数是可以当作容器类型的元素
a = demo              #demo没有加（），是作为调用函数，无返回值的
a()                  #a加了（）可以被调用，输出了  nihao
print()

b = demo()          #输出nihao   1000
print(b)
print()

c = a()
print(c)           #输出nihao   1000