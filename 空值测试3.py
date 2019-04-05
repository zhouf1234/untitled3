#atm入口
import time
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
                if users_atm not  in ['1', '2', '3', '4']:
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
                if users_atm == '2':
                    while True:
                        tix = input('是否确认提现(是/否): ')
                        if tix in ['是', '否']:
                            break
                        else:
                            print('请输入：是/否')
                    if tix == '是':
                        jine = int(input('请输入提现金额：'))
                        if jine > data[users_card]['yue']:
                            print('余额不足')
                        else:
                            res = jine * .05
                            print('可以提现，手续费金额为%s' % res)
                            qit = input('操作成功，是否还选择其他服务(yes/no)：')
                            if qit == 'yes':
                                continue
                            if qit == 'no':
                                times = 1
                if users_atm == '3':
                    ti = time.strftime('%d')
                    print('今天是本月%s日' % ti)
                    if ti == '10':
                        print('今天是还款最后一天,过期未还，按欠款总额 万分之5 每日计息')
                    elif ti == '14':
                        print('今天是信用卡账单日，请在下月十号之前还清账单')  # 下一行print当月总的消费金额
                        user_shop = {}
                        with open('shop.txt', 'r', encoding='utf-8')as f:
                            for line in f:
                                line_list = line.replace('\n', '').split(' ')
                                user_shop[line_list[0][:4]] = int(line_list[0][5:])
                                print('账单金额：%s' % user_shop['sale'])
                    while True:
                        huank = input('今天是否给信用卡还款(是/否): ')
                        if huank in ['是', '否']:
                            break
                        else:
                            print('请输入：是/否')
                    if huank == '是':
                        user_jine = {}  # 读取文件中的信息，将信用卡金额的信息放入字典
                        user_card = {}
                        user_pswd = {}
                        with open('xinyongka.txt', 'r', encoding='gbk')as f:
                            for line in f:
                                line_list = line.replace('\n', '').split(' ')
                                user_jine[line_list[2][:3]] = int(line_list[2][4:])
                                user_card[line_list[0][:4]] = int(line_list[0][5:])
                                user_pswd[line_list[4][:4]] = int(line_list[4][5:])
                        while True:
                            huank_card = int(input('请输入信用卡号：'))
                            # huank_pswd = int(input('请输入银行卡密码：'))
                            if huank_card != user_card['card']:
                                print('信用卡账号错误或不存在，请重新输入！')
                                continue
                            else:
                                print('信用卡账户存在！')
                                huank_jin = int(input('请输入您的还款金额：'))
                                if huank_jin <= data[users_card]['yue']:
                                    print('还款成功')
                                    qit = input('操作成功，是否还选择其他服务(yes/no)：')
                                    if qit == 'yes':
                                        times = 0
                                        break
                                    if qit == 'no':
                                        times = 1
                                        break
                                else:
                                    print('余额不足')
                            break
                if users_atm == '4':
                    with open('yinhangkazhuanz.txt', 'r', encoding='gbk')as f:
                        dat = eval(f.read())
                        # for keys,i in data.items():
                        # print(keys,i)
                        # print('收款人:%s  银行卡号%s' % (keys, i['card']))
                    while True:
                        zhuan_name = input('请输入收款人姓名：')
                        zhuan_card = int(input('请输入要转账的银行卡号：'))
                        if zhuan_name not in dat:
                            print('账号不存在，请重新输入')
                            continue
                        if zhuan_card != dat[zhuan_name]['card']:
                            print('该银行卡号填写错误！')
                            continue
                        else:
                            print('银行卡账号存在，可以转账！')
                            zhuanz_jine = int(input('请输入转账金额：'))
                            res = data[users_card]['yue'] - zhuanz_jine
                            print('转账成功！您的余额为:%s' % res)  # 文件内容没有修改，无法修改文件金额
                            qit = input('操作成功，是否还选择其他服务(yes/no)：')
                            if qit == 'yes':
                                times = 0
                            if qit == 'no':
                                times = 1
                                break
            break







