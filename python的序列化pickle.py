import pickle

user_info = {'name':'丹丹','age':19,'add':'上海','grade':'py01'}
print(user_info)
print(type(user_info))

#序列化：二进制数据
str = pickle.dumps(user_info)
print(str)
print(type(str))

#把序列化的数据存入文bat件
with open('pick.bat','wb')as f:
    f.write(str)
