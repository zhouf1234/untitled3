# 类和对象属性
# class类属性，类可用，对象也可用
#Person对象属性只能对象使用，不能print(person.sex)
class Person:
    # height，weight类属性，类可用，对象也可用
    height=200
    weight=100
    def __init__(self):
        # sex，age，sleep对象属性只能对象使用
        self.sex='male'
        self.age=20
        self.sleep=lambda :print('sleep')

    def eat(self):
        print('好！')
    #
    # def sleep(self):
    #     print('睡吧')

p1=Person()
print(p1.sex,p1.age,p1.height,p1.weight)
print(Person.height, Person.weight)
p1.sleep()
print()

p2=Person()
print(p2.height,p2.weight)
p2.eat()
Person.eat(p2)

