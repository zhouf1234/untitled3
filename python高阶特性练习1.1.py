# 生成器 斐波那契数列
def feibonaqie(n):
    def get_number(n):
        if n <= 0:
            return 0
        if n <= 1:
            return 1
        return get_number(n-2) + get_number(n-1)
    for i in range(n):
        yield get_number(i)

g = feibonaqie(10)
for i in g:
    print(i)


# 斐波那契数列第二种方法
def feibonaqie(n):
    if n <= 1:
        yield 0
        return
    if n <= 2:
        yield 0
        yield 1
        return
    n1 = 0  # 上上个
    n2 = 1  # 上一个
    yield n1
    yield n2
    for n in range(2, n):
        curr = n1 + n2
        yield curr
        n1 = n2
        n2 = curr

for i in feibonaqie(10):
    print(i)