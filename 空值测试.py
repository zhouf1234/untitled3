while True:
    users = input('请选择你的身份(用户：输入1/工作人员：输入2): ')
    if users in ['1', '2']:
        break
    else:
        print('请输入：1/2')
if users == '1':
    print('欢迎使用ATM！')
    while True:
        users_card = int(input('请输入您的银行卡号：'))
        users_pwsd = int(input('请输入密码：'))
        with open('yinhangka2.txt', 'r', encoding='gbk')as f:
            data = eval(f.read())
        if users_card not in data:
            print('账号不存在，请重新输入')
            continue
        if users_pwsd != data[users_card]['pwsd']:
            print('密码错误！请重新输入')
            continue
        else:
            print('登录成功！')
            times = 0
            while times == 0:
                users_atm = input('请选择服务(查看账户信息：选择1/提现：选择2/信用卡还款：选择3/转账：选择4): ')
                if users_atm not in ['1', '2', '3', '4']:
                    print('请输入：1/2/3/4')
                    continue
                if users_atm == '1':
                    res_o = data[users_card]['name']
                    res_t = data[users_card]['card']
                    res_th = data[users_card]['yue']
                    print('您的账户信息为：账户名：%s  银行卡号：%s  账户余额：%s' % (res_o, res_t, res_th))
                    qit = input('操作成功，是否还选择其他服务(yes/no)：')
                    if qit == 'yes':
                        continue
                    if qit == 'no':
                        times = 1
            break


