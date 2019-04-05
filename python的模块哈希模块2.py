#哈希模块的加密安全性
import hashlib

#提高加密安全性,加key
key = 'goole_99'
md5 = hashlib.md5(key.encode('utf-8'))
md5.update('12345'.encode('utf-8'))
print(md5.hexdigest())