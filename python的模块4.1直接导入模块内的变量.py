# 把模块内的变量 直接导入进来
# from dandan import read

# 导入模块中多个 变量或函数
# from ... import将模块中的变量 加入到当前的全局作用域中
# from dandan import read, get_info, name, age, set_name

# 导入模块 给模块中的变量起别名
from dandan import read as r, get_info as gi, name,age
from functools import reduce
from collections.abc import Iterator, Iterable

name = '莉莉'

r()               #输出dandan.py文件中的read函数的print
print(name)       #莉莉。直接用模块把dandan.py文件中的变量name导入进来，并在这里重新赋值为莉莉
print()

 #read()
#get_info()
print(name)
print(age)
