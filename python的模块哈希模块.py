#导入哈希模块：摘要运算，加密用,存密码
import hashlib

msg = '12345'
#md5加密:
# 哈希算法又称摘要算法、散列算法。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串(通常用16进制的字符串表示)，多用于加密
#hashlib模块主要提供了如下哈希方法
#md5 32位16进制数 128位2进制数
#sha1 40位16进制数 160位2进制数
#sha224 56位16进制数 224位2进制数
#sha256 64位16进制数 256位2进制数
#sha384 96位16进制数 384位2进制数
#sha512 128位16进制数 512位2进制数
hash = hashlib .md5(msg.encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.md5('12'.encode('utf-8'))
hash.update('34'.encode('utf-8'))
hash.update('56'.encode('utf-8'))
print(hash.hexdigest())
print()

#sha1加密
hash = hashlib.sha1()
hash.update(msg.encode('utf-8'))
print(hash.hexdigest())

hash = hashlib.sha1('12345'.encode('utf-8'))  #同上的一样的结果显示
print(hash.hexdigest())
print()

#sha224加密
hash = hashlib.sha224()
hash.update(msg.encode('utf-8'))
print(hash.hexdigest())

#sha256加密
hash = hashlib.sha256()
hash.update(msg.encode('utf-8'))
print(hash.hexdigest())

#sha384加密
hash = hashlib.sha384()
hash.update(msg.encode('utf-8'))
print(hash.hexdigest())

#sha512加密
hash = hashlib.sha512()
hash.update(msg.encode('utf-8'))
print(hash.hexdigest())