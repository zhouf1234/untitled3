#列表的元素是1-100组成的数字:

# 生成一个列表：
list = [ i for i in range(1,101)]   #i对应i
print(list)

#列表是1-10数字的平方
list = [ i * i for i in range(1,11)]
print(list)

#列表2的0次方一直到2的10次方
list = [2 ** i for i in range(0,11)]  #运算符**：幂，返回x的y次幂
print(list)

#列表1-100中所有偶数
list = [i for i in range(1,101) if i % 2 == 0]
print(list)
print()

#列表的操作符:组合+，重复*
print([1,2,3,'a'] + ['a','b','c','d'])
print([10,20,30] * 5)
print()

# 往空列表添加内容
list = []
for i in range(1,10):
    # print(i)
    if i not in list:
        list.append(i)
print(list)
print()

#列表中的列表的生成
A6 = [[i, i * i] for i in range(10)]
print(A6)  #[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36]。。。]


