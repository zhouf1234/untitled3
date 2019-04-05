#定义函数
#普通参数和命名关键字参数本来用*隔开
#但是如果中间有可变参数的话，不用*，*args就隔开了

def demo(a,b,*args,name,age,**kwargs):
    print(a,b,args,kwargs,name,age)
#调用
demo(1,2,'aa','bb','cc',99,88,name='dandan',age=15,add='shanghai',phone=123456)
print()

# 只有命名关键字参数 和 关键字参数
def fn(*, name, age, **kwargs):
    pass

# 有可变参数  命名关键字参数
def fn01(*args, name, age):
    pass