#from 包，包，包.文件 import 变量
#from后import导入的模块，必须是明确的一个不能带点，否则会有语法错误
from aaa import ccc

from aaa import api
api.get_info()
print(ccc.name)
