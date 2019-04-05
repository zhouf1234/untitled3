import re

#^    表示字符串开始边界
#$	 表示字符串结束边界    ，开始和边界尽量都写上
while True:
    #获取用户的输入
    email = input('请输入邮箱：')
    #定义邮箱的正则表达式
    email_pattern = '^[\w-]+@[\w-]+(\.\w+){1,2}$'
    # 验证邮箱：
    if re.match(email_pattern,email) != None:
        print('邮箱格式正确')
        break
    else:
        print('错误')

while True:
    #获取用户的输入
    qq_q = input('请输入qq：')
    # 验证qq：
    if re.match('^\d{5,11}$',qq_q) != None:
        print('qq格式正确')
        break
    else:
        print('错误')


while True:
    #获取用户的输入
    phone = input('请输入座机号：')
    #定义正则表达式
    phone_pattern = '^\d{3,4}[-]?\d{7,8}$'
    # 验证座机号：
    if re.match(phone_pattern,phone) != None:
        print('座机号格式正确')
        break
    else:
        print('错误')


