class Person:
    school='阳光幼儿园'

    def __init__(self):
        self.name='丹丹'


p1=Person()
# 使用对象的方法（属性）时，先看有无此属性，如果没有再看类有无此属性
print(p1.school)            #阳光幼儿园
# 给对象改school属性后
Person.school='夏天小学'
print(p1.school)            #夏天小学
print()

p2=Person()
print(p2.school)            #夏天小学