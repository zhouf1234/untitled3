boy_firends = ['李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦']
print(boy_firends)

#删除其中一个
del boy_firends[2]
print(boy_firends)

#list.pop([index]) ，不写下标则默认删除最后一个
boy_firends.pop()
print(boy_firends)

#删除列表中第一个和值匹配的元素
boy_firends.remove('刘备')
print(boy_firends)
print()

#给列表添加元素
boy_firends.append('赵云')      #直接给列表后添加元素
print(boy_firends)

boy_firends.insert(5,'项羽')   #list.insert(index, obj) 指定位置插入元素
print(boy_firends)
print()

#统计
print(boy_firends.count('赵云'))   #list.count(obj) 统计某个元素在列表中出现的次数
#查找索引下标
print(boy_firends.index('赵云'))   #list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
#反转列表
boy_firends.reverse()               #list.reverse() 反转列表
print(boy_firends)
print()

#在列表后面追加一个列表:数据类型必须相同才能追加（列表/集合/元组）
boy_firends.extend([10,20,30])
boy_firends.extend({1,2,3})

print(boy_firends)