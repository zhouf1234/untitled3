#reduce把一个回调函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算


#从模块中导入reduce
from functools import reduce
#实现列表中所以元素的和
L = [1,2,3,4,5,6,7]
def add(x,y):
   # print(x,y)  #用于方便理解reduce是如何计算
    return x+y
print(reduce(add,L))       #28
print()

#把列表中的数，拼成一个整数
num = [1,2,3,4,5,6,7]
def num_reduce(x,y):
    print(x,y)         #用于方便理解reduce是如何计算
    return x * 10 + y
res = reduce(num_reduce,num)
print(res)               #1234567
print(type(res))