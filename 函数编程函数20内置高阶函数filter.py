# filter 高阶函数  搞列表   过滤
#和map()类似，filter()也接收一个函数和一个序列。filter用于元素过滤
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
s = [1,2,3,4,5,6,7,8,9]
#把列表中 <3的值去掉，返回原列表
def filter_fn(item):
    #if item<3:
        #return False
    #else:
        #return True
    return item<3
print(list(filter(filter_fn,s)))
