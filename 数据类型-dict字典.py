# 定义字典 dict
#user_info = ['丹丹', 17, '上海', 13838385438]
# 字典的value可以是任意类型   key只能是不可变类型(str\int\float\complex...)
user_info = {'name':'丹丹', 'age':17, 'address':'上海', 'phone':13838385438, 'boyfriends':['王思聪','马云','刘强东','比尔盖茨']}    #字典

print(type(user_info))
print(user_info)


# 获取其中的某个成员
print(user_info['address'])

#修改某个成员的值
user_info['age'] += 1

print(user_info)