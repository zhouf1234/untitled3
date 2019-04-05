#定义列表
numbers = [1,2,3,4,5,6,7]
#要求得到一个新列表，新列表是numbers这个列表中每个元素的3次方
#map一般用来处理列表：map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# new_number = []
# for i in numbers:
#     new_number.append(i ** 3)
#
# print(new_number)
def map_fn(ite):
    return ite **3
res=list(map(map_fn,numbers))  #把map的返回结果变为列表,不写list的话结果。。。。
print(res)
#res2=map(map_fn,numbers)
#print(list(res2))            #也可，同res结果一样的


#处理字符串，把字符串都变为大写
msg = 'Hello nihao'
def upper_str(item):
    if item >= 'a' and item<= 'z':
     return chr(ord(item)-32)     #Unicode编码转换，
    else:                          #ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
        return item
#return item.upper()  #尝试一下直接返回值是大写
print(''.join(list(map(upper_str,msg))))