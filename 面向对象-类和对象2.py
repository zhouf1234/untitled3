# 定义类
class Student:
    # 初始化函数,self就是一个形参，传进来的就是s1和s2的对象
    # 只写（self）参数，则相当于把name，age等属性写死了，所在传参里，把name，age等参数也写进去，后面s1，s2可以分别传值
    def __init__(self,name,age,sex,school):
        # print(self)
        # self.name='anan'
        # self.age=19
        # self.sex='女'
        # self.school='阳光幼儿园'
        self.name=name
        self.age=age
        self.sex=sex
        self.school=school

    # 写技能，操作
    def eat(self):
        print('能吃')

    def sleep(self):
        print('能睡')

    def study(self):
        print(self.name+'爱学习')

    def say(self):
        print('我叫%s，性别%s，今年%s,来自%s' %(self.name,self.sex,self.age,self.school))

    pass

# 实例化对象，写属性
s1=Student('bobo',23,'男','西湖幼儿园')
print(s1.name,s1.age,s1.sex,s1.school)
# 写技能，学习
s1.eat()
s1.sleep()
s1.study()
s1.say()
print()

s2=Student('coco',23,'女','东湖幼儿园')
print(s2.name,s2.age,s2.sex,s2.school)
s2.study()