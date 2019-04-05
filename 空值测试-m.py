x=[1,2,3]
x.insert(1,4)  #指定位置插入元素，1为位置
print(x)
print()

#定义一个list，打印出每个元素出现的次数
mylist=['D','G','H','D','G','H','D','G']
myset=set(mylist) #myset是另外一个列表，里面的内容是mylist里面的无重复项  
for item in myset:
 print("元素 %s 出现了 %d 次" %(item,mylist.count(item)))
# times = mylist.count('D')
# print(list(myset))
print()

A0 = dict(zip(('a','b','s','d','e'),(1,2,3,4,5)))
A1 = range(10)                               #range(0,10)
A2 = sorted([i for i in A1 if i in A0])     #[]
A3 = sorted([A0[s] for s in A0])        #[1, 2, 3, 4, 5]
A4 = [i for i in A1 if i in A3]         #[1, 2, 3, 4, 5]
A6 = [[i, i * i] for i in A1]   #[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25]...]
print(A0,A1,A2,A3,A4)
print(A6)
print()