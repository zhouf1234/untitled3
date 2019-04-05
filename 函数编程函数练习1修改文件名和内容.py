#1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作

import os
def sun(a,b):
    with open('users.txt', 'w', encoding='gbk') as f:   #写一个文件:文件操作
        f.writelines(b)
    file_name = (a+'.txt')                              #给文件重命名
    os.rename('users.txt', file_name)
    print(a,b)

E='filefile'                  #要修改的文件名
F=['a','b','c','d','e']      #要修改的文件内容
sun(E,F)


#第二种方法:有点复杂了解

def sum(filename,count,*,encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as f:   #写一个文件:文件操作
        f.write(count)
# edit_file('data.txt', 'hello 同志')