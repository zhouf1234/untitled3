#统计s='hello alan alan say hello sb sb'中每个字母的个数，放在一个字典中
s='hello alan alan say hello sb sb'
b = {}
for i in s:
    keys = s.count(i)
    b.setdefault(i,keys)
    #print(i)
    #print(keys)
print(b)
print()

#统计s='hello alan alan say hello sb sb'中每个单词的个数，放在一个字典中
s='hello alan alan say hello sb sb'
l = s.split(' ')    #分割字符串 成 列表
b = {}              # 定义字典
for i in l:
    b[i] = l.count(i)        #上例的方法也可以用，这个更简洁
print(b)
print()