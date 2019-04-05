users_yanzheng =input('请输入用户名：')
if users_yanzheng == 'admin':
    print('超级管理员')
elif users_yanzheng == 'tom':
    print('普通管理员')
elif users_yanzheng =='jack' or users_yanzheng== 'rain':
    print('业务主管')
else:
    print('普通用户')