#LEGB是Python中名字(变量)的查找顺序
#LEGB  代表名字查找顺序: locals -> enclosing function -> globals -> __builtins_
#locals         是函数内的名字空间，包括局部变量和形参   本作用域(名字空间)
#enclosing     外部嵌套函数的名字空间（闭包中常见）        上层作用域（名字空间）
#globals     全局变量，函数定义所在模块的名字空间          全局作用域(名字空间)
#builtins     内置模块的名字空间
name = '100'
age = 16
add = '上海'
def demo():
    name = '200'
    age = 20
    int = 1
    def fn():
        name = '300'
        print(name)   #使用的是本作用域额变量:显示300
        print(age)    #上层作用域    ：20
        print(add)    #全局作用域的变量1  :上海
        print(int)    #不给int赋值，也可的
    fn()
demo()
print()

#列表去重
list = [1,2,3,4,5,62,3,2,1]
#print(list(set(list)))会报错，因为内层已经变set，所以外层不能list显示