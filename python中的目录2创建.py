#导入一个模块用来操作目录
import os

#创建
# os.mkdir('./data')     #当前文件夹创建一个文件夹
#创建,如果不存在则创建
if not os.path.exists('./data'):    #exists:判断文件是否存在
    os.mkdir('./data')

#创建10个目录，目录分别是01-10
for i in range(1,11):
    dirname = './data/'+ (('0'+str(i))if i < 10 else str(i) )  #给目录名不足十加0：02 03 .。。
    if not os.path.exists(dirname):           #判断：创建,如果不存在则创建
       os.mkdir(dirname)

#创建多层目录
