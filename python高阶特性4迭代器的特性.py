l = [1,2,3,4,5]
def fn(x):
    print(x)
    return 0
map_l=map(fn,l)
#next(map_l)      #1 :写了next（）才会执行，不写就不执行，迭代器的惰性计算特点，不占内存，无法获取长度
#next(map_l)      #2  ：next的值只是x的值，不是返回值

# for i in map_L:
#     print(i)

list(map_l)   #转为列表

#print(len(map_L))
