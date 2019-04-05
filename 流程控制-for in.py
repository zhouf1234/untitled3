#使用for in 遍历顺序访问 的数据类型:可遍历所有的容器类型
user_list = ['曹操','刘备','关羽','张飞']
num_tuple = [12,23,45,56,3]
msg = 'hello dandan'

#遍历输出，列表中的每个元素
for user in user_list:        #遍历列表
    print(user)
print()

sum = 0
for i in num_tuple:         #遍历元组
    sum += i
print(sum)
print()

for m in msg:               #遍历字符串
    print(m)
print()


#for in 同样可以遍历字典，遍历出来的时字典的key（关键字）
user_dict = {'name':'dandan','age':17,'address':'上海'}
for o in user_dict:
    print(o,user_dict[o])
print()

#遍历集合和不可变集合
user_set = {1,5,4,6,7,8,5,9}    #遍历集合
for p in user_set:
    print(p)
print()

print(list(user_set))

