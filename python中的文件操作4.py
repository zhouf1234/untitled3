#文件读取
with open('文件例.txt','r',encoding = 'gbk') as f:
    data = f.read()   #文件中的内容全部读取
    print(data)
    print()

#重置光标
    f.seek(0)
    print(f.readline(),end='') #读一行
    print(f.readline(),end='') #读一行
    print(f.readline(),end='') #读一行
    print()

    #重置光标
#f.seek(0)
#print(f.readlines())