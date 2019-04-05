l = [i for i in range(1,10,2)]      #列表生成器
print(l)

#生成器表达式
#1-10数字
g1 = (i for i  in range(1,11))
for i in g1:
    print(i,end= ' ')
print()

g2 = (i for i  in range(1,11)if i % 2 == 0)
for i in g2:
    print(i,end= ' ')
print()

#得到小写字母a-z组成的生成器
g3 = (chr(i) for i in range(97, 123))
for i in g3:
    print(i, end=' ')
