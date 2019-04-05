with open('file.txt','r') as f:
    print(f.readable())
    print(f.writable())
    print(f.encoding)
    print(f.closed)
    print(f.name)
print(f.closed)
#f.readable() #文件是否可读
#f.writable() #文件是否可写
#f.encoding #如果文件打开模式为b,则没有该属性
#f.closed #文件是否关闭