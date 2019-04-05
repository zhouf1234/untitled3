import re

#匹配成功，返回对象，失败返回none，格式如下：
#re.match('字符串形式的正则表达式','要验证的字符串')

# 原子
print(re.match('\u0061', 'a'))


#验证手机号
phone_num = '12345678901'
print(re.match('\d{11}',phone_num))   #是不是11位数字

# 验证手机号
phon_num = input('请输入您的手机号:')

if re.match('1[356789]\d{9}', phon_num) != None:
    print('输入正确！')
else:
    print('您输入的不是手机号')