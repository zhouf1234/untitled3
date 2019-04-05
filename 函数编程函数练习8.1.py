#  有个列表，此次用匿名函数来做的
# 根据成绩进行排名，  从大到小
#2. 取出成绩最高的人
#3. 取出成绩最低的人
#4. 给每个人成绩+10分
#5. 去掉成绩小于60的人
users = [
    {'name':'曹操', 'score':67},
    {'name':'刘备', 'score':45},
    {'name':'诸葛亮', 'score':77},
    {'name':'司马懿', 'score':112},
    {'name':'司马光', 'score':17},
    {'name':'司马迁', 'score':87},
]
new_users = sorted(users,key=lambda item:item['score'],reverse=True)   #排序
for item in new_users:
    print(item)
print()

max_users = max(users,key=lambda item:item['score'])                #2取出成绩最高的人
#其中 匿名函数lambda只能做简单的处理，解题方法也是多的
print(max_users)
print()

max_users = min(users,key=lambda item:item['score'])                #3取出成绩最低的人
print(max_users)
print()

def map_call(item):                                                  #4.给每个人成绩+10分
    item['score']+=10
    return item
users_new = list(map(map_call,users))
for item in users_new:
    print(item)
print()

filter_users=list(filter(lambda user:user['score']>=60,users))        #5. 去掉成绩小于60的人
for item in filter_users:
    print(item)