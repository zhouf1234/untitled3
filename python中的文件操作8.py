with open('文件例.txt', 'r', encoding='gbk') as f:
    # f.write('OK')
    print(f.read(3))
    print(f.read(3))
    print(f.read(3))

    f.seek(0) #光标移动到最前面
    f.seek(14) # 单位是字节

    print(f.read())