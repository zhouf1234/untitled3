#循环输出0~10
i = 1   #循环变量
while i <= 10:
    print(i,end = ' ')
    i += 1      #循环一个操作i=i+1
print()

#输出0-10之间的奇数
b = 1
while b<= 10:
      if  b % 2 != 0:
       print(b,end=',')
       b += 2