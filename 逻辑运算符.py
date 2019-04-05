print(not True)
#逻辑非：表达式的结果是布尔值
print(not 100)
print(not 0)    #数字里面只有0对应的是false，其他数字都是true
print(not -10)
print(not 'abc')    #false
print(not '')       #true
print()

#逻辑与：逻辑与输出结果取决于两边表达式都要成立
print(10>3 and 4>1)  #true
print(100 and 90)   #90：100（true）作为表达式的布尔值成立，90（true）也成立，最后一次执行时90，所以是90
print(0 and 10)     #0：0（false）作为表达式的布尔值不成立，所以10不会再判断，所以是0
print()        #隔开

#逻辑或
print(3 > 1 or 1 > 1)   #true
print(10+2 or 100)      #12:第一个作为表达式成立，所以12
print(10-10 or 1+1)     #2:第一个不成立，第二个成立
