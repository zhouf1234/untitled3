#导入一个模块用来操作目录
import os

#目录或文件判断：os.path.isdir(path) 如果path是一个存在的目录，则返回True。否则返回False
for file in os.listdir('./data3'):         #os.listdir:data3下所有文件夹目录
    filename = './data3/' + file
    filetype = '目录'if os.path.isdir(filename)else'文件'  #os.path.isdir:判断是否是目录
    print('文件名：%s   类型：%s'%(file,filetype) )
#print(file,end = ' ')
