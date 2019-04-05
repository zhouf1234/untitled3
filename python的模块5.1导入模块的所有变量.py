# 导入模块中 所有的变量:from 模块 import *
from dandan import *
from lili import *
# from lili import lili_fn, lili_info, user, address
from os import path
from os.path import abspath, join

print(name)                #dandan
print(age)                #18
get_info()              #输出dandan.py文件中的get_info函数的print
read()                 # #输出dandan.py文件中的read函数的print

print()

# print(user)
# print(address)
lili_fn()
lili_info()
# print(user)

print()

print(path.abspath('./'))        #前路径转为绝对路径，并输出，前面由path模块