#导入一个模块用来操作目录
import os

#查看文件的目录或信息
#print(os.stat('./文件夹名'))
print(os.stat('./'))     #当前文件夹下目录：结果已包含最后该文件夹存取时间和最后修改时间
print()

#print(os.listdir('../data01'))
for file in os.listdir('../'):   #上一个文件夹下所有文件夹目录
    print(file)
print()

#os.path.getsize(path) 返回文件/目录的大小：了解
#print(os.path.getsize('./day07笔记.md'))
#print(os.path.getsize('./01-查看文件或目录信息.py'))
print(os.path.getsize('../'))      #上一个文件夹的大小
print(os.path.getsize('./'))       #当前文件夹大小
print()

#os.path.getatime(path) 返回path所指向的文件或者目录的最后存取时间:时间戳，以秒计,(window下是 创建时间)
print(os.path.getatime('../'))
#os.path.getmtime(path) 返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime('./'))
