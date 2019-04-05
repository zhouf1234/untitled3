class Animal:
    def __init__(self,hobby):
        self.hobby=hobby

    def run(self):
        print('在跑')
# Dog类属性重写了
class Dog(Animal):
    def run(self):
        print('狗在跑')
class Cat(Animal):
    pass

d=Dog('骨头')
d.run()             #狗在跑
print(d.hobby)


c = Cat('老鼠')
c.run()
