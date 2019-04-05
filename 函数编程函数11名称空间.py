#先加载内置空间，在加载全局空间，在执行文件的过程中如果调用函数，则临时产生局部名称空间
age = 100        #在全局命名空间，所有作用域就是全局的
def fn():
    name = 'xiaoli'     #名称空间只在fn（），内置空间
    print(name)
    print(age)
fn()                   #输出xiaoli   100，两个print
print(age)             #输出100
#print(name)           #报错，name这个变量在内置空间，不在全局