#数字序列  连续
a = range(3,10)
print(a)
print(type(a))

for i in a:
    print(i,end = ' ')              #输出3~9数字,不写end=’‘是竖排
print()

#循环输出1-100
for m in range(1,101):              #输出1-100
    print(m,end = ' ')
print()

#计算88*89*90.。。。*100
res = 1
for i in range(88,101):
    res *= i
print(res)
print()

#输出1-50的偶数，循环了50 次
for i in range(1,51):
    if i % 2 == 0:
        print(i,end = ' ')
print()

#输出1-50的所有奇数
for s in range(1,51,2):
    print(s,end = ' ')
print()

#输出10 9 8 7 6 5 4 3 2 1
for i in range(10,0,-1):
    print(i,end = ' ')


