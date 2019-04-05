#import aaa   #导入aaa实际导入的是包里的_init_模块

#直接导入api和path模块
import aaa.api
import aaa.path

#导入包里的包
import aaa.bbb                     #aaa文件夹下bbb文件夹下的_init_.py这个文件
import aaa.ccc.c

print(aaa.name)                       #aaa文件夹下的_init_.py这个文件
print(aaa.description)
aaa.get_info()
print()

print(aaa.api.name)                 #import aaa.api模块：aaa文件夹下的api.py这个文件
print(aaa.api.description)
aaa.api.get_info()
print()

aaa.path.fn()                     #import aaa.path：aaa文件夹下的path.py这个文件
print()

print(aaa.ccc.name)               #import aaa.ccc.c:aaa这个包里的包ccc文件夹下的init.py文件
print(aaa.ccc.description)
aaa.ccc.get_info()
print()

print(aaa.ccc.c.name)            #import aaa.ccc.c:aaa这个包里的包ccc文件夹下的c.py文件
print(aaa.ccc.c.description)



