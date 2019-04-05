cu=[]
def fn(a,y):
    x=a+y
    cu.append(a)
    if x<100:
        return fn(y,x)
print(fn(0,1))
print(cu)
print()

#第二种：循环的方法
a=0
b=1
i=1
cu2 = []
while i<10:
    c=a+b
    # print(c)
    cu2.append(c)
    a=b
    b=c
    i += 1
print(cu2)
print()

#第三种：递归函数
def fi(n):
    if n<=1:
        return n
    else:
        return fi(n-1)+fi(n-2)
d=9
for i in range(d):
    print(fi(i))
