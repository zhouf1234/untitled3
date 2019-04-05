#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
with open('file.txt','r',encoding='gbk')as f:
    pass

#声明变量：关键字参数，两个**
#自定义函数get_info
def get_info(**users):
    print(users)
#调用
get_info(name='丹丹',age=19,phone=123456)      #关键字参数在函数内部自动组装为一个dict
get_info()
get_info(num=100)
print()

#定义函数，既有普通参数，又有关键字参数
#关键字按照key=value的形式定义的实参
#无需按照位置为形参传值
#注意的问题：
 #  1. 关键字实参必须在位置实参右面
  # 2. 对同一个形参不能重复传值

def test_fn_01(a,b='xiao',**kwargs):
    print(a,b,kwargs)

#调用
test_fn_01(1,'a',name='d',age=16)
test_fn_01(1,name='d',age=16)
print()

#定义函数，普通参数，又有可变参数
def test_02(a,b,c,*args):
    print(a,b,c,*args)
#调用
test_02(1,2,3,4,4,4,4)
test_02(100,'dan','nihao',23,23)
print()

#定义函数，普通参数a,b,，又有可变参数*args，关键字参数**kwargs
#组合使用参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def test_03(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

#调用
test_03(1,2,3,4,4,4,4)
test_03(100, 200, 'hello', 100, 23, 100, name='jack', age=18)
print()

