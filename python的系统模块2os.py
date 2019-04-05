import os

os.chdir('./')
print(os.getcwd())   #获取当前的工作目录，有盘符
print(os.curdir)    #返回当前目录: ('.')
print(os.pardir)    #获取当前目录的父目录字符串名：('..')

os.system("rm -rf day15-1")  #运行shell命令，直接显示
print(os.environ) #获取系统环境变量
