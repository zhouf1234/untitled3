import os,sys

# 说明导入的是内置模块os，而不是自定义模块 os
#os.mkdir('test')

for path in sys.path:
    print(path)