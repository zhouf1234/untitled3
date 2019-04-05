n = None    #不允许小写，只能大写
print(type(n))
print(n)

#被动产生
def demo():
    1+1
    print(demo())       #未获取到想要的数据，或者函数没有return，默认返回None

