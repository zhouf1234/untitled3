# 定义类
class Student:
    pass

# 实例化对象
s1=Student()
# 给对象添加属性
s1.name='anan'
s1.age=18

print(s1)
print(s1.name,s1.age)
print(type(s1))
print(isinstance(s1,Student))
print()

# s1,s2内存中位置不一样，所以不相等的
s2=Student()
print(s2)
print(type(s2))
print(isinstance(s2,Student))
print()

a  = int(10)
print(a)
print(type(a))
