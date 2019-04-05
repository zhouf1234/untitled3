#生成器里面1-100的数字
def gen_fn():
    for i in range(1,101):
        yield i

f = gen_fn()
print(f)
#print(next(f))              #写了next（）才会执行，不写就不执行,此次方便记忆回顾

#l=list(range(1,101))
for i in f:
    print(i)