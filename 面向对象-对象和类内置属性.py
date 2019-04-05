class Person:
    school='阳光大学'

    def __init__(self):
        self.name='小赵'

    def eat(self):
        pass


p=Person()
p.age =100

print(dir(p))
print(p.__dict__)  #返回字典，只包含对象（实例化属性）属性{'name': '小赵', 'age': 100}
print(p.__dir__()) #同dir（）
print(p.__class__)
print(p.__module__)
print(p.__doc__)
print()

print('hello'.__class__)  #等同于type,<class 'str'>
print(100.10.__class__) #<class 'float'>
print((100).__class__) #<class 'int'>