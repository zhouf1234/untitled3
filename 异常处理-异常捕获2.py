Iter = (i for i in range(1,5))
try:
    print(next(Iter))
    print(next(Iter))
    print(next(Iter))
    print(next(Iter))
    print(next(Iter))   #没有5，异常捕获处理了，显示：错了
except:
    print('错了')
