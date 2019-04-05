#九九乘法表的正反显示
for i in range(1,10):      #遍历9次,9列9行
    for j in range(1,i+1):
        print('%d*%d=%d' %(j,i,i*j),end = ' ')    #%d占位运算符
    print()

for i in range(9,0,-1):                     #第一个循环：9列
    for j in range(1,i+1):                  #第二个循环：9行
        print('%d*%d=%d' %(j,i,i*j),end = ' ')
    print()