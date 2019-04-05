#自定义一个函数print_hello()
def print_hello(): #无参
    pass
#Python函数先定义 再调用
#函数名(print_name)本质上就是变量名
#定义阶段
def print_name():
    print('nihao')
    print('222')
    print('ddd')
    print('....end....')
#调用阶段才会执行
print_name()
print_name()
print_name()
print()

def fn_02():
    b = 1 + 1



#定义函数
def fn_01():
    a = 10 * 10
    return a          #返回值会作为函数表达式的值
#调用    函数调用本身就是表达式，该表达式的值就是 函数的返回值
res = fn_01()
print(res)
print(res + 9)
print()
print(fn_01())
print(fn_01() + 20)
print()

print(fn_02())         #fn_02没有写返回值，所以显示空值
print()

#print不是return，函数中有print,函数调用了就会执行
def fn_03():
    print('hello!nihao!')

print(fn_03())    #函数中已经输出一次，此次之后返回none空值
print()

#python函数可以return多个值，函数调用表达式的值是个元组
def fn_04():
    return 20,30,'hello',['1','2','3']  #返回值是个元组
print(fn_04())                             #输出返回值
print()

#return会终止函数的执行，retrurn后面的不会执行
def fn_05():
    print('你好')
    return 150
    print('aaa')
fn_05()           #只输出 你好，因为函数输出了(printt)
print()

#两个return：retrurn后面的不会执行，只执行第一个return
def fn_06():
    return 4*4        #函数终止
    return 3          #不会执行到了
fn_06()               #此次不会输出任何值，因为没有输出fn_06()
print(fn_06())        #输出16
print()
print(10 + fn_06())   #输出26
print()

def fn_07(a):
    return a    #返回值是个元组
print(fn_07('111111111'))         #输出返回值
print()

def fn_08(a,b,*args):
    return a,b,args                   #所以返回值是个元组
print(fn_08(2,59,'nihao'))           #调用值是个元组
#G=(2,4,'key')               #简化写法有点问题暂时不用与return
#fn_08(G)