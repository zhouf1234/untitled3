#  有个列表，没有使用匿名函数我的作业
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
def sor(item):
    return item['score']
print(sorted(users,key=sor,reverse = True))  # 根据成绩进行排名，从大到小

res=max(users,key=sor)                   #2. 取出成绩最高的人
print(res['name'])
#print(max(users,key=sor))

res=min(users,key=sor)                  #3. 取出成绩最低的人
print(res['name'])
#print(min(users,key=sor))

#for i in users:                         #4. 给每个人成绩+10分
    #i['score']+=10
    #print(i)
#print()
def so(ite):
    ite['score']+=10
    return ite
print((list(map(so,users))))

#for j in users:                         #5. 去掉成绩小于60的人
    #if j['score']>60:
        #print(j)
def s(it):
    return it['score']>=60
print((list(filter(s,users))))





