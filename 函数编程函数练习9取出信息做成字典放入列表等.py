#文件内容如下,标题为:姓名,性别,年纪,薪资
#要求: 从文件中取出每一条记录放入列表中,
# 列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式
#1、 根据1得到的列表,取出薪资最高的人的信息
#2、 根据1得到的列表,取出最年轻的人的信息
#3.根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
#4.根据1得到的列表,过滤掉名字以a开头的人的信息

users = []
with open('file-five.txt','r',encoding='gbk')as f:  #读文件信息
   for line in f:
      list_line = line.replace('\n', '').split(' ')    #不写此行，遍历出来的信息都是字符串
      users.append({                                     #给列表添加元素
         'name':list_line[0],
         'sex':list_line[1],
         'age':list_line[2],
         'salary':list_line[3]
      })
print(users)

max_list=(max(users,key=lambda item:item['salary']))  #1、 根据1得到的列表,取出薪资最高的人的信息
print(max_list)
max_list=(min(users,key=lambda item:item['age']))  #2、 根据1得到的列表,取出最年轻的人的信息
print(max_list)
print()

#4.根据1得到的列表,过滤掉名字以a开头的人的信息
new_users = list(filter(lambda item:not item['name'].startswith('a'), users))
for user in new_users:
    print(user)
print()



