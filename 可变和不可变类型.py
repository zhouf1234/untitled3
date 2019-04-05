#id type  value
#id()  type()
#id一样，type和value一定相等
#type和value一样，id不一定相等
a = 100
b = 100
print(id(a))
print(id(b))
print(a is b)           #是数字，不可变类型，值一样，所以id一样，如果值不一样，id也不一样
print()

a = [10.230000000,100]    #是列表，是可变类型，值一样，所以id不一样，如果值不一样，id 也不一样
b = [10.230000000,100]      #两个
print(id(a))
print(id(b))
print()

#在id不变的情况下，value可以变，则称为可变类型：如列表 字典 集合
users = ['曹','诸葛','孙']
print(id(users))
users[1] = '贾'
print(id(users))
print()

users = [10,20,30]    #相当于给users重新赋值
print(id(users))
print()

#不可变类型：value一旦改变，id也改变，如： 数字、字符串、元祖、布尔
age = 101
print(id(age))
age = 121
print(id(age))

