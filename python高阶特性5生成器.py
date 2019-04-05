#函数中，有yield 关键字，该函数的返回值就是生成器对象
from collections .abc import Iterator
def func():
    print('第一次')
    yield 1
    print('第二次')
    yield 2
    print('第三次')
    yield 3
g = func()
print(g)                            #得到的是一个生成器<generator object func at 0x00000200B5AC7B48>
print(type(g))                      #<class 'generator'>
print(isinstance(g,Iterator))          #ture

next(g)              #输出：第一次；写了next（）才会执行，不写就不执行
next(g)             #第二次
next(g)             #第三次
#print(next(g))     #1,第一次


# for i in g:
#     print(i)


