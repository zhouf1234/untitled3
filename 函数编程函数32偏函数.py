#偏函数,了解
print(int('11111'))
print(int('11111',base=2))         #将字符串转换成整型，二进制
print(int('11111',base=16))        ##将字符串转换成整型，十六进制

def int2(str):
    return int(str,base=2)
print(int2('11111'))
print()

import functools         #functools.partial使用时要用的模块
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
int2 = functools.partial(int,base=2)          #可以将十进制直接转成二进制
open_utf = functools.partial(open, encoding='utf-8')

print(int2('10001'))

