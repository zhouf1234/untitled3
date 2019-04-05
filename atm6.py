#atm管理接口：添加账户、用户额度，冻结账户等
while True:
    users = input('请选择你的身份(用户：输入1/工作人员：输入2): ')
    if users in ['1', '2']:
        break
    else:
        print('请输入：1/2')
if users == '2':
    print('欢迎进入管理员后台！')
    while True:
        users_admin = input('请输入您的用户名：')
        users_pw = int(input('请输入密码：'))
        with open('yinhangkaadmin.txt', 'r', encoding='gbk')as f:
            da = eval(f.read())
        if users_admin not in da:
            print('账号不存在，请重新输入')
            continue
        if users_pw != da[users_admin]['pwsd']:
            print('密码错误！请重新输入')
            continue
        else:
            print('登录成功！欢迎%s使用后台' %da[users_admin]['name'])
            tims = 0
            while tims == 0:
                users_ad = input('请选择服务(添加账户：选择a/用户额度：选择b/冻结账户：选择c/退出：选择d): ')
                if users_ad not in ['a', 'b', 'c','d']:
                    print('请输入：a/b/c/d')
                    continue
                if users_ad == 'a':
                    users_ca = int(input('请输入要添加的银行卡号：'))
                    users_p = int(input('请输入要添加的银行卡密码：'))
                    users_name = input('请输入要添加的银行卡用户名：')
                    with open('yinhangka2.txt', 'r', encoding='gbk')as f:
                        de = eval(f.read())
                    if users_ca in de:
                        print('该银行卡号存在，请重新输入：')
                        continue
                    else:
                        print('添加新账户成功！')
                        with open('yinhangka3.txt', 'a', encoding='gbk')as f:  #若是添加到yinhangka2，格式不一无法读
                            f.write('%s:{"card":%s,"pwsd":%s,"name":"%s"\n' %(users_ca,users_ca,users_p,users_name))
                if users_ad == 'd':
                    times = 1
                    break
            break