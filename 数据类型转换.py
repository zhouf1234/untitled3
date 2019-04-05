#转为整型
num = int('123456')
#num = int('123.123')     转不了
#num = int('abc')        转不了
#num = int('123abc')     转不了
num = int(True)        #0
num = int(False)         #0
num = int(10.56)
print(type(num))
print(num)
print()

#转为字符串:几乎都能转
print(str(100))
print(str(10.23))
print(str(True))
print(str([1,2,3]))
print()

#转为容器：列表，集合，字典,元组等
users_info = {'name':'dandan','age':17}
print(list(users_info))

users = {'淡淡','丽丽','花花'}
print(dict(users))

#列表转为元组
tuple_list = tuple(users)
print(tuple_list)

#转为不可变集合

