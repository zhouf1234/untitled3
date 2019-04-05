#导入一个模块用来操作目录
import os

#如果文件存在，则删除
#os.remove('./tst.txt')

if os.path.exists('./tst.txt'):        #exists:判断文件是否存在
    os.remove('./tst.txt')             #如果在就删除

#删除目录:rmdir；删除单级空目录，若目录不为空则无法删除，报错
#os.rmdir('./data')
#os.rmdir('./data/01')

#删除目录:rmdir('./data/01')   #删除单层
#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
#os.removedirs('./data/01')
