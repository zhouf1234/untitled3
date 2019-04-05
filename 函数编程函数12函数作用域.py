x = 100       #全局变量
def fn():
    a = 33    #局部变量
    print(x)
    print(a)
def func():
    fn()       #调用fn（）的返回值
#print(a) 不能调用局部变量a
fn()                  #输出两行：100   33
func()                #输出两行：100   33



