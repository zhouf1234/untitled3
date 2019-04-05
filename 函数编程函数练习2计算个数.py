#2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

def sum(a):
    b={}
    for i in a:
        keys=a.count(i)
        b.setdefault(i, keys)    #如果要获取的key不存在，除了返回默认值外，还把该key添加到 字典中
    print(b)                   #计算的是每个字符的个数

D='my name is zhou,year is 2018.'
sum(D)

#第二种方法：解题
def count_str(msg):
    res_dict = {           #一个字典模板
        'digit':0,        #digit:数字
        'letter':0,       #letter：字母
        'space':0,        #space：空格
        'else':0          #else：其他
    }
    for char in msg:
        if char.isdigit():               #判断是否是数字
            res_dict['digit'] +=1
        elif char.lower() in [chr(i)for i in range(97,123)]:  #Unicode编码转换来判断是不是字母
            res_dict['letter'] += 1
        elif char == ' ':               #判断是不是空格
            res_dict['space'] += 1
        else:                          #判断是不是其他
            res_dict['else'] += 1
    return res_dict
print(count_str('hello,1991'))