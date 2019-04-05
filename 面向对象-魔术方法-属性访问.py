class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    # # 访问不存在的属性时触发，返回值即属性值
    def __getattr__(self, item):
        # print('没有属性%s' %item)
        print('__getattribute')
        return 0

    # # 访问属性不论（add）是否存在，都会触发返回值
    # def __getattribute__(self, item):
    #     print('__getattribute')
    #     return 'hello'

    # 给属性赋值时触发
    def __setattr__(self, key, value):
        print('__steattr')
        self.__dict__[key]=value



p=Person('anan',18,'女')
print(p.add)
print(p.name)
print()

p.name='bobo'
p.email='111@qq.com'
print(p.name)