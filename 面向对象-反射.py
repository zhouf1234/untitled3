# 反射：以字符串形式去操作对象属性
class Stu:
    school='阳光'
    def __init__(self,name,age,grade,sex):
        self.name=name
        self.age=age
        self.grade=grade
        self.sex=sex

    def eat(self):
        print('吃')

s=Stu('a',19,'一班','male')

print(getattr(s,'name'))            #a
print(getattr(s,'add','上海'))    #上海
print(getattr(s,'age',36))      #19
print()

# 设置属性值
setattr(s,'age',24)
print(s.age)                    #24


#删除属性
delattr(s,'grade')
print(s.__dict__)               #{'name': 'a', 'age': 24, 'sex': 'male'}
print()

#判断一个属性是否存在
print(hasattr(s,'grade'))       #false
print(hasattr(s, 'name'))