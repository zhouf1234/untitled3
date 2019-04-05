#魔术方法：构造-初始化-析构
class Person:
    # 构造方法,用来构造实例,return什么，就得到什么;用的也少
    def __new__(cls, *args, **kwargs):
        # return 100
        print('被构造了')
        return super().__new__(cls)

    # 初始化方法,在__new__()之后被调用，用来给实例属性赋值
    def __init__(self,name):
        self.name=name
        print('%s被初始化了' %self.name)

    #析构方法，对象销毁时执行
    def __del__(self):
        print('%s被析构了' %self.name)


p=Person('p')
print(p.name)

p1=Person('p1')
print(p1.name)