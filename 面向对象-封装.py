class Student:
    school='阳光幼儿园'
    def __init__(self,name,age,sex):
        #私有属性，外部无法访问，只能内部访问,封装属性
        self.__name=name
        self.__age=age
        self.__sex=sex

    def say(self):
        print('我叫%s，性别%s，今年%s' % (self.__name, self.__sex,self.__age))


s = Student('anby',16,'male')
s.__age=10          #相当于新增了一个公开属性__age

s.say()
print(s.__age)      #10
# print(s.__name) #已经无法访问，因为被封装了