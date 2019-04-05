#3 使用生成器 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
#同递归来做的，只能得到一个值
def fi(n):
    if n<=1:
        yield 0
        return         #如果不写return，则n=1时，会得到0，0，1
    if n<=2:
        yield 0
        yield 1
        return
    yield(list(fi(n-2)).pop()+list(fi(n-1)).pop())
g=fi(10)
for i in g:
    print(i)
print()

