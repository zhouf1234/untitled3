class Fib:


    def __getitem__(self, item):
        a,b=1,1
        for i in range(0,item):
            a,b = b,a+b
        return a


f=Fib()

print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])