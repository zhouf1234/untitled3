#globals() # 返回字典 全局作用域下所有的变量
## locals()返回字典 本作用域(局部作用域)下所有的变量
name = 'hello'
def demo():
    age = 100
    pass

print(globals())  #查看所有全局变量
print(locals())  #不在函数空间内则和globals显示一样,#返回本作用域下的变量
print()

def fn():    #如果是fn(a,b),a,b也在本作用域下
    num = 100
    print(globals())
    print(locals())   #在函数空间内,本作用域下
fn()            #输出num：100
#fn(100,200)     #如果是fn(a,b),a,b各自实参100，200
