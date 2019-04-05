#导入一个模块用来操作目录
import os

#文件重命名
#os.rename(src, dst)  重命名或者移动文件和目录  不光可以修改文件的名字还能修改文件的存储位置
if os.path.exists('./'):             #exists:判断当前文件夹是否存在文件
    os.rename('./data','./data3')   #存在则重命名data为data3

if os.path.exists('./data'):
    os.rename('./data', './data3')

os.rename('空.txt', 'fei.txt')    #当前文件夹下的文件重命名

# 文件的移动
#os.rename('./数据', '../数据')
#os.rename('./tst.txt', '../tst.txt')