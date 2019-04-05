#1. 可以提现，手续费5%
#用信用卡提现
def tix():
    while True:
        tix = input('是否确认提现(是/否): ')
        if tix in ['是', '否']:
            break
        else:
            print('请输入：是/否')
    if tix == '是':
        user_car = {}  # 读取文件中的信息，将信用卡卡号的信息放入字典
        user_pws = {}
        user_dict = {}
        with open('xinyongka.txt', 'r', encoding='gbk')as f:
            for line in f:
                line_list = line.replace('\n', '').split(' ')
                user_car[line_list[0][:4]] = int(line_list[0][5:])
                user_pws[line_list[4][:4]] = int(line_list[4][5:])
                user_dict[line_list[2][:3]] = int(line_list[2][4:])
        while True:
            tix_card = int(input('请输入信用卡号：'))
            tix_pswd = int(input('请输入信用卡密码：'))
            if tix_pswd != user_pws['pwsd'] or tix_card != user_car['card']:
                print('用户名或密码错误，请重新输入')
                continue
            else:
                print('信用卡账号密码登录成功！')
                jine = int(input('请输入提现金额：'))
                if jine > user_dict['yue']:
                    print('余额不足')
                else:
                    res = jine * .05
                    print('可以提现，手续费金额为%s' % res)
            break















