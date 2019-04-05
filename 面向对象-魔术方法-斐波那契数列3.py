class Fib:
    def __getitem__(self, item):
        # return type(item)
        # return type(item),得出item（即f[0:9]）的数据类型为slice
        # 判断，如果是切片类型就取到其开始和结束的
        # if isinstance(item,slice):
        #     print(item.start)
        #     print(item.stop)
        #     return

        if isinstance(item,int):
            a,b=1,1
            for i in range(item):
                a,b=b,a+b
            return a
        elif isinstance(item,slice):
            L=[]
            a, b = 1, 1
            for i in range(item.start,item.stop):
                L.append(a)
                a, b = b, a + b
            return L[item.start:item.stop]


f=Fib()
print(f[0])
print(f[1])
print(f[2])
print()
print(f[0:9])   #[1, 1, 2, 3, 5, 8, 13, 21, 34]
