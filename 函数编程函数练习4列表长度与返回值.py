#4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def daxiao(*args):
    if len(args)>2:
      print(args[0:2])    #输出值

B=[1,2,3,4,5,6]
daxiao(*B)


#第二种方法：返回值,调用的是列表，返回的也是列表
def daxiao(a):
    if len(a)>2:
        return a[0:2]   #返回前两个长度的内容
    else:
        return a[::]    #返回整个列表

print(daxiao([1,2,3,4,5,6]))
