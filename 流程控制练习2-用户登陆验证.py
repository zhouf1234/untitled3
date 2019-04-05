users_name = input('请输入用户名：')
users_pass = int(input('请输入密码：'))

if users_name == 'admin' and users_pass ==123456:
    print('登录成功')
else:
    print('登录失败')
