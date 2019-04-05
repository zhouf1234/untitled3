#定义全局变量
name = 'riri'
#定义函数
#就是要在函数中修改全局变量用global，global关键字用来在函数或其他局部作用域中使用全局变量。
def fn():
    global name
    name = 'aiaiaiai'
    print(name)
fn()          #输出aiaiaiai
print(name)#如果要使这个name的值riri变成aiaiai，用修改全局变量关键字global，此次已改变
print()

def foo():
#print(name)    #写在前面会报错
    name = 'ci'
    print(name)  #使用本层变量name
foo()             #输出ci
print()

#nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
def fn_wrapper():
    add = '上海'
    def fn_inner():
        # 修改上层作用域的address
        nonlocal add    #声明该变量是上层作用域的变量add
        add = '北京'
        print(add)      #输出北京,内置空间局部变量
    fn_inner()
    print(add)          #不写nonlocal会输出上海 ，写了是北京
#调用
fn_wrapper()          #输出北京  北京  两行，两个print
#print(add)            #没有定义全局add的值，报错
print()

age = 10         #全局变量
def test_wrp():
    age = 20      #局部变量
    def test_inner():
        global age
        age = 30      #局部变量
        print(age)    #不写global是30，写了是30
    test_inner()
    print(age)        #不写global是20，写了是20
test_wrp()     #输出30  20两行
print(age) #不写global是10，写了是30；如果要使这个age的值10变成30，用修改全局变量关键字global
print()

