lambda name,age:19               #与函数有相同的作用域，但是匿名意味着引用计数为0，使用一次就释放，除非让其有名字
fn = lambda x,y=10:x+y             # 可以把匿名函数赋值给变量使其有名，但这样没意义了
print(fn(1,2))
print(fn(8))
print()

from functools import reduce         #用reduce要使用的模块
#匿名函数可以当回调函数使用
salaries={
    '发哥':3000,
    '铭哥':100000000,
    '丹丹':10000,
    '老朱':2000
}

#取出工资最少的人
print(min(salaries,key=lambda key:salaries[key]))   #老朱
print()

print(reduce(lambda x,y:x+y, [1,23,2,2,2,23,23]))   #求和76