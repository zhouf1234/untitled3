class Stu:
    school='阳光小学'
    add='lundon'

    def __init__(self):
        self.name='coco'

s=Stu()
print(s.name)
print(s.add)        #类属性
print(s.__dict__)   #所有实例属性
# print(s.__base__)不能操作，报错

print()

print(Stu.add)
print(Stu.__dict__)  #类的实例属性
print(Stu.__bases__)    #用的类的元类属性
