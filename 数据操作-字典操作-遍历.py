# 创建一个字典  丹丹的男朋友
boy_friend = {'name': '武大郎', 'age':67, 'height':145, 'weight':180}


# 遍历字典中每一个成员
print(boy_friend.keys())  #得到字典中所有的key组成的 列表
print(boy_friend.values())  #得到字典中所有的值 组成的 类表
print(boy_friend.items())  #列表，成员是key和value组成的元组

# 遍历 字典中所有 值
for i in boy_friend.values():
    print(i)
print()

# key 和 value 一起遍历出来
for key,vals in boy_friend.items():
    print(key, vals)