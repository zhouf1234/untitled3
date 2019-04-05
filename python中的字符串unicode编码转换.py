#对于单个字符的Unicode编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('a'))          #Unicode编码转换
print(ord('好'))
print(chr(88))
print(chr(20320))
print()

#对字符串进行编码
print('hello'.encode('utf-8'))
b = b'hello'
print(b)
print(type(b))

print('keyi'.encode('utf-8'))
print('中文'.encode('utf-8'))

print(b'hello'.decode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print()

# 完成程序，输入汉字， 输出汉字对应的 unicode编码（16进制显示）
print('----------unicode转换-----------')


while True:
    str = input('请输入字符串：')
    # 处理用户输入的字符串
    unicode_str = ''
    for char in str:
        unicode_num = ord(char)
        unicode_hex = hex(unicode_num)
        unicode_str += '\\u' + unicode_hex[2:]
    print('unicode编码为：')
    print(unicode_str)
    print()