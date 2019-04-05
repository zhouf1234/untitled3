# 用户进入程序 选择 登录还是 注册实现
while True:
    choise = input('请输入：1(登录)或者2(注册)：')
    if choise in ['1', '2']:
        break
    else:
        print('请输入1或者2')

# 注册
if choise == '2':
    while True:
        print('--------注册-----------')
        user_name = input('请输入用户名：')
        user_pwd = input('请输入密码：')
        user_repwd = input('请再次输入密码：')
        # 验证 密码
        if (user_pwd != user_repwd):
            print('两次输入的密码不一致，重新开始注册')
            continue
        # 把用户信息写入文件
        with open('users.txt', 'a') as f:
            f.write('\n%s %s' %(user_name, user_pwd))
        print('注册成功！请登录')
        choise = '1'
        break

# 登录
if choise == '1':
    # 从文件中读取 用户信息 放入字典中
    user_dict = {}
    with open('users.txt', 'r') as f:
        for line in f:
            line_list = line.replace('\n', '').split(' ')
            user_dict[line_list[0]] = line_list[1]
    # 开始验证
    while True:
        user_name = input('请输入用户名：')
        user_pwd = input('清输入密码：')
        # 验证判断用户名
        if user_name not in user_dict:
            print('用户名不存在！ 请重新登录')
            continue
        # 验证判断 密码
        # print(user_dict)
        if user_pwd != user_dict[user_name]:
            print('密码错误！ 请重新登录')
            continue
        print('登录成功！')
        break


# 登录成功后 想干嘛就干嘛
