class Fib:
    # 返回一个斐波那锲数列组成的 列表
    def __get_fib_list(self, len):
        L = []
        a, b = 1, 1
        for i in range(len):
            L.append(a)
            a, b = b, a + b
        return L


    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__get_fib_list(item+1)[item]
        elif isinstance(item, slice):
            return self.__get_fib_list(item.stop)[item.start:item.stop]
        else:
            return None



f = Fib()

print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print()

print(f[0:10])
print(f[2:10])
print()

print(f['hello'])