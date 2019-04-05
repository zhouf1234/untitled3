#有如下列表，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
a = [11,22,33,44,55,66,77,88,99,90]
b = {'c':[],'d':[]}           #创建一个只有key的字典，其value是一个列表,所以用[]
#遍历列表
for i in a:
    if i > 66:
        b['c'].append(i)      #b['c']：获取字典的key指向的value，value是列表，所以.append添加列表
    else:
        b['d'].append(i)
print(b)


