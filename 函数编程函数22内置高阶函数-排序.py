#python内置的sorted()函数就可以对list进行排序
L = [1,-2,322,444,-77,9,22,-5]

print(sorted(L))  #从小到大
print(sorted(L,reverse = True))#从大到小

#按照绝对值排序，从小到大
print(sorted(L,key=abs))

#按成绩排序，从小到大
K = [('a',55),('b',99),('c',77),('d',88)]
def sor(item):
    return item[1]
print(sorted(K,key=sor))