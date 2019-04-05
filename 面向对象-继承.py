
#子类cat，dog会继承父类animal中所有属性和方法
class Animal:
    def __init__(self,hobby):
        self.hobby=hobby

    def run(self):
        print('在跑')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 实例化
d=Dog('骨头')
d.run()
print(d.hobby)