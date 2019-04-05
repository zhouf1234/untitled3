#导入一个模块用来操作目录
import os

#处理成绝对路径：对于计算机来讲，绝对路径更好
filename = './data3/tst1.txt'
print(os.path.abspath(filename))        #os.path.abspath()  转为绝对路径

#相对路径更短，处理成绝对路径
#绝对路径有利于跨平台性，不同平台的，绝对路径不一样

print(os.path.isabs('./data3/tst1.txt'))                    #os.path.isabs()  判断是否是绝对路径
print(os.path.isabs('C:\PycharmProjects\data3\tst1.txt'))
print()

#路径拼接:os.path.join
#'./data ./data/'
print(os.path.join('./data3/','tst1.txt'))
print()

filename = 'C:\PycharmProjects\data3\\tst1.txt'
print(os.path.split(filename))         #os.path.split()  把路径分割成两部分   目录部分和文件部分
print(os.path.basename(filename))      #os.path.basename() 提取路径中的文件部分
print(os.path.dirname(filename))       #os.path.dirname()  提取路径中的目录部分
print()

print(os.path.normcase('./data3/tst1.txt'))   #os.path.normcase()  返回当前平台的标准路径