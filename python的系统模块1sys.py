import sys

print(sys.version)          #获取Python解释程序的版本信息
print(sys.argv)            #命令行参数List，第一个元素是程序本身路径
print(sys.path)         #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)    #返回操作系统平台名称

sys.exit(0)          #结束进程
print('hello 丹丹')       #不会显示