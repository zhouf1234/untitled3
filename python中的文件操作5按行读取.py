#按行读取
with open('文件例.txt','r',encoding = 'gbk') as f:
    for line in f:
        print(line)

