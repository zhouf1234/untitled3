# r :打开文件:只读模式【默认模式，文件必须存在，不存在则抛出异常】
with open('文件2.txt','r',encoding = 'gbk') as f:
    print(f.read())


#  w 只写模式【清空原先的内容 文件不存在则创建一个文件】
with open('文件4.txt','w',encoding = 'gbk') as f:
    f.write('hello dandan')


#  a 方式追加写:之追加写模式【不可读；不存在则创建；存在则只追加内容】
with open('文件例.txt','a',encoding = 'gbk') as f:
    f.write('你好吗亲\n')
print()


# b：二进制格式读取r，二进制格式写入w
with open('文件例.txt','rb') as rf,open('文件4.txt','wb') as wf,open('02.jpg','rb') as image_f:
    print(rf.read())
    wf.write(b'hello\xc3\xc7')
    print(image_f.read())
print()

#w+ r+ a+：
with open('文件例.txt', 'r+') as rf, open('文件例.txt', 'w+') as wf:
    rf.write('丹丹')
    print(wf.read())
