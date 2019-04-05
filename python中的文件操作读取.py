#打开一个文件
f = open('文件例.txt','r')     # 通过变量对文件进行操作
#读取文件
data = f.read()
f.close()    #关闭文件操作
print(data)

#读取文件:第二个方法:更简洁
with open('文件例.txt','r') as f:
    data = f.read()
print(data)

#指定要打开的文件
path1 = '文件例.txt'                #文件路径，此处是当前文件夹
path = '../untitled3/hello.py'    #打开一个.py文件:同级目录

with open(path,'r',encoding = 'utf-8') as f:
    data = f.read()
print(data)

