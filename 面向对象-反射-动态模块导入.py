# 此次引入的是user.py文件作为模块，输入：user
modName=input('请输入要导入的模块：')

# 动态导入模块：__import__(模块名)方法
con=__import__(modName)
method = input('请输入要执行的方法：')  #输入：fn或者test
if hasattr(con,method):
    func=getattr(con,method)
    func()
else:
    print('该模块没有这个方法')