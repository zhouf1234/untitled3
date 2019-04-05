class Person:

    def __init__(self,name,age):
        #__封装属性，使其私有属性，外部无法访问，只能内部访问
        self.__name=name
        self.__age=age

    #查看age
    def get_age(self):
        return self.__age

    #给age赋值，不能随便写年龄，有条件
    def set_age(self,value):
        #条件1：年龄必须使数字
        if not isinstance(value,int):
            raise TypeError('年龄必须使数字')
        # 条件2：年龄必须有个范围
        if value<0 or value>200:
            raise TypeError('年龄范围错误')
        self.__age=value

    def __fn1(self):
        pass

    def __fn2(self):
        pass

    def __fn3(self):
        pass

    # 方法
    def fn(self):
        self.__fn1()
        self.__fn2()
        self.__fn3()



s = Person('nana',233)
print(s.get_age())
s.set_age(123)
print(s.get_age())
