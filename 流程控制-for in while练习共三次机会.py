#循环,用户登陆（三次机会重试）
for i in range(0,3):  #三次循环
    name = input('用户名：')   #获取用户输入
    pwd = input('密码')
    #验证用户输入
    if name == 'admin' and pwd == '123':
        print('成功')
        break                   #成功就跳出循环
    else:
        print('失败')
        print('还有%d次机会' %(2 - i))
