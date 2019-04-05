#求所有参数和
def sum(*args):
    s=0
    for i in args:
        s += i
    return s
#调用
print(sum(1,3,4,52,4,6,73,9))
nums=[1,2,3,4,21,31,42]
print(sum(*nums))
print()

#定义
def fn01(a,b):
    print('%s和%s去跳舞'%(a,b))
#调用
L = ['小李','小妹']
fn01(*L)           #列表用*
print()


def fn02(a,b,*args):
    print(a,b,args)

M=[1,2,3,4,21,31,42]
fn02(*M)
print()


def fn03(*,name,age,**kwargs):
    print(name,age,kwargs)

U = {'add':'shangh','name':'dandan','age':16}
fn03(**U)         #字典用**
print()

#普通参数a,b,，又有可变参数*args，命名关键字参数name、age，关键字参数**kwargs
#组合使用参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def fn04(a,b,*args,name,age,**kwargs):
    print(a,b)
    print(args)            #输出一个元组
    print(name,age)        #调用函数中，name：dandan，age：16，命名关键字函数显示dandan 16
    print(kwargs)          #输出一个字典

P= [1,2,3,4,5,6]
B= {'add':'shangh','name':'dandan','age':16,'phone':123456}
fn04(*P,**B)
