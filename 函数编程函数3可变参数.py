#内置参数，就是 可变参数数量的函数：一个*，后面加变量名
#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
#可变参数在函数调用时自动组装为一个tuple元组
# number是元组

print(max(2,4,17,44,7,9,22))              #输出最大值
print(min(13,44,23,11,5,3,2,7,9,110,34))  #输出最小值
print()

#定义函数，实现所有参数的和
def sum(*args):
    sum_number = 0
    for i in args:       #遍历参数args
        sum_number += i   #给实参求和
    return sum_number    #返回sum_number
#调用
#sum(10,3,6,8,2,55,33)
print(sum(2,3,5,8,4,1))  #可变参数调用时自动组装为一个元组
print()

#所有参数的平方并求和：平方和
#定义函数
def sum_mi(*args):
    sum_num = 0
    for i in args:
        sum_num += i * i
    return sum_num
#调用
print(sum_mi(2,3,5,8,4,1))
print(sum(11,22,13,42,23,34,34,4655,5676,23,334))
print(sum_mi(2,3))