#22、 编写日志装饰器，
# 实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，
# 日志文件路径可以指定

#如何将函数输出的字符串写入日志文件？
#指定文件路径？

def log(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        with open('file-three.txt','a',encoding='gbk')as f:
            f.write('%s-%s-%s %s:%s:%s \n'%(2017,7,21,11,12,11))
        return res
    return wrapper

@log
def f1():
    return 1
f1()
