#hamc模块：同样进行hash运算的，必须要指定key
#import hmac

#hm = hmac.new(key, 要密码的内容，digestmod='MD5/SHA256..')
#hm.hexdigest()
import hmac

key = 'google_88'

hm = hmac.new(key.encode('utf-8'), '123456'.encode('utf-8'), digestmod='SHA1')

print(hm.hexdigest())