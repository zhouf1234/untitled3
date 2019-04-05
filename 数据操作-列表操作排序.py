nums = [1,4,78,12,5,9,22]
print(nums)
#排序：默认从小到大
nums.sort()
print(nums)
print()
#排序：从大到小
def my_sort(n1):
    return -n1
nums.sort(key=my_sort)
print(nums)
print()

#定义一个列表
girl_firends = [
    {'name':'冰冰','age':45,'height':'170'},
    {'name':'晶晶','age':25,'height':'160'},
    {'name':'燕燕','age':33,'height':'175'},
    {'name':'格格','age':18,'height':'180'},
]
# 按年龄排序从小到大
print(girl_firends)
def girl_sort(n2):        #回调函数
    return n2['age']     #按年龄排序
girl_firends.sort(key=girl_sort)
print((girl_firends))