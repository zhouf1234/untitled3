#定义函数
def print_mes(a,b,c):
    print('%s和%s还有%s一起去吃饭' %(a,b,c))
print_mes('明明','可可','天天')
#print_mes('小明','小可')           #报错
print()

#定义函数
#普通参数b,c可以有默认值，即默认参数，则调用的时候按位置调用，有默认值的参数 必须在后面
def print_me(a,b='安安',c='娥娥'):
    print('%s和%s还有%s一起去吃饭' %(a,b,c))
print_me('水水')
print_me('娜娜','卡卡')
print_me('燕燕','婷婷','么么')