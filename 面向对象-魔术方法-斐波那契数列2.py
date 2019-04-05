# 1. 斐波那锲对象升级  f[0] f[1] f[0:10]  f[9:100]
class Fib:
    def __getitem__(self, item):
        a,b=1,1
        for i in range(0,item):
            a,b = b,a+b
        return a


f=Fib()
print(f[0])
print(f[1])
print()

list=[ i for i in range(0,10)]
for i in list:
    print(f[i])

print()
list2=[ i for i in range(9,100)]
for j in list2:
    print(f[j])

