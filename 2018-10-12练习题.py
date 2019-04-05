#1：可变类型：    list列表      dict字典       set集合
#不可变类型int     float    complex    boolean     none    str     tuple  Frozenset

#：2按成绩排序
students = [
    {'name':'曹操', 'age':48,'score':98.5},
    {'name':'丹丹','age':18, 'score':78},
    {'name':'陈真','age':28, 'score':60},
    {'name':'张无忌','age':25, 'score':88},
    {'name':'令狐冲','age':31, 'score':72},
]
new_users = sorted(students,key=lambda item:item['score'],reverse=True)   #排序
for item in new_users:
    print(item)
print()

#3:将01的内容复制到02
with open('01.txt','a',encoding = 'utf-8') as f:      #创建一个txt01
    f.write('111111111111111111')
with open('02.txt','a',encoding = 'utf-8') as f:       #创建一个txt02
    f.write('2222222222222222222')

with open('01.txt', 'r') as rf, open('02.txt', 'a') as af:    #将01的内容复制到02
    af.write(rf.read())

#4:第二题的列表，去掉年纪小于30的成员
def s(it):
    return it['age']>=30
print((list(filter(s,students))))

#5:可迭代器和可迭代对象的区别：迭代器(Iterator) 一定是 可迭代的，可迭代对象(Iterable) 不一定 是迭代器


#6：列表生成器创建一个列表，成员是2的0次方到2的10次方
list = [2 ** i for i in range(0,11)]
print(list)
print()

#7:有字符串hello world，请对其进行hash加密，使用md5
import hashlib
msg = 'hello world'
hash = hashlib .md5(msg.encode('utf-8'))
print(hash.hexdigest())
print()

#8:创建装饰器，计算函数运行时间
import time
def run_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print('the function running use time is %s:秒' %(end_time - start_time))  #输出运行时间
        return res
    return wrapper
#定义函数，并使用装饰器
@run_time
def get_dir_size(filename):
    for i in range(1,100000):
        a = i * i
get_dir_size('hello,hello')
print()

#9:如何判断python文件时被当模块引用还是当作脚本直接运行
if __name__ == '__main__':
    print('被当作脚本，直接运行！')
else:
    print('被当做模块用!')
print()

#10:递归函数实现删除一个非空目录

import os
os.mkdir('./fn')         #创建一个文件夹
for i in range(1,11):    #给文件夹创建目录
    dirname = './fn/'+ (('0'+str(i))if i < 10 else str(i) )
    if not os.path.exists(dirname):
       os.mkdir(dirname)

def get_dir_size1(pathname):     #删除目录及其中文件
    if os.path.isdir(pathname):
        for file in os.listdir(pathname):
            filename = os.path.join(pathname,file)
            get_dir_size1(filename)
        os.rmdir(pathname)                     #删除目录
    else:
        os.remove(pathname)                    #删除文件
print(get_dir_size1('./fn'))

