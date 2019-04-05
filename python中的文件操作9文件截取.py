with open('file.txt','r+',encoding= 'utf-8') as f:
    print(f.read(6))
    f.truncate(20)                       #文件光标从头开始截取20 字节
