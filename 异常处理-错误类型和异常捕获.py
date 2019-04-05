# 编译过程错误：。。。。。
# print(num)
# NameError: name 'num' is not defined:属性不存在

# def fn():
#     pass
# fn(100)


# IndentationError: unindent does not match any outer indentation level:缩进错误
# if True:
#      print('ok')
#     print('l')


#异常捕获：无法判断是否有错误，又不想系统崩溃时
#异常捕获1:一个一个捕获错误，2更好
# FileNotFoundError：存在则不显示，不存在就显示：文件不存在，此次显示不存在
#不影响下方的print
# try:
#     f=open('11.txt')
# except FileNotFoundError:
#     print('文件不存在')
# except NameError:
#     print('名字不存在')
# except TypeError:
#     print('类型错误')

#异常捕获2：Exception可以捕获所有的错误，不会使系统崩溃的
#不影响下面的
try:
    f = open('11.txt')
except Exception as error:
    print('报错误了')
    #把错误信息提示反馈出来
    print(error)


print('ok')
print('1')
