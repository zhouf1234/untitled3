#求1-100的所有数的和
j = 0
for i in range(1,101):   #range(1,101)指遍历1到100这些数字
    j += i
print(j)
print()

#输出 1-100 内的所有奇数
for i in range(1,101,2):
    print(i,end = ' ')
print()

#输出 1-100 内的所有偶数
for i in range(2,102,2):
    print(i, end = ' ')
print()

#求1-2+3-4+5 ... 99的所有数的和
res = 0
for i in range(1,100,2):
    res -= i+(-(i+1))
print(res)
print()

#whil循环写上题
i = 1               #循环条件
sum = 0
while i< 100:
    if i % 2 != 0:  #if循环，是奇数就加，是偶数就减
        sum += i
    else:
        sum -= i
    i += 1
print(sum)
