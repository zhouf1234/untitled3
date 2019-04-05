class Person:
    school='阳光大学'

    def __init__(self):
        self.name='小赵'

    def eat(self):
        pass


p=Person()
#dir,返回一个列表，显示所有对象可访问的属性
print(dir(p))
#type,返回对象的类，类就是类型
print(type(p))
#isinstance，判断对象是否是该类的实例
print(isinstance(p,Person))
print()

print(hasattr(p, 'name'))
print(hasattr(p, 'eat'))
print(hasattr(p, '__dir__'))