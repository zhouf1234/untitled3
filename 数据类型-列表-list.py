#声明列表
companys = ['google','facebook','apple','alibaba','baidu']
print(type(companys))
print(companys)

#列表中的每个成员叫做元素，每个元素都有下标索引，获取某个元素的值
print(companys[2])
#修改某个元素的值：字符串不可以，只有列表可以改
companys[3] = 'jd'            #将下标为3的alibaba改为jd
print(companys)
print()

#列表元素的数据类型，任意类型
list = ['你好',100,23234,34,True,None,1.666,[10,20,30]]
arr = [[1,2,3],['a','b','c'],[[50,60],[70,80]]]
print(list)
print(list[7][1])
print(arr[2][1][0])
