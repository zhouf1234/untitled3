 #导入多个模块
# import os
# import sys,
# import functools
# import collections
# import dandan

# 一行导入多个模块
# import os, sys, functools, collections, dandan

# 导入多个摸块的同时 给模块取别名
import os, sys as s, functools, collections, dandan as dan


print(os.path.abspath('./'))     #当前路径转为绝对路径，并输出

dan.read()                       #输出dandan.py文件中的read函数的print
dan.get_info()                   #输出dandan.py文件中的get_info函数的print
print(s.path)         #.sys.path是个列表，包含 当前的目录，项目的目录 以及 第三方模块的一些目录
print(dan.name)                 #dandan

dan.set_name('曹操')
print(dan.name)              #输出曹操


