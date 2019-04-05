#购物车结账，调用信用卡接口结账
def shop_two():
    print('欢迎使用信用卡!')
    while True:
        jiez = input('是否继续(是/否): ')
        if jiez in ['是', '否']:
            break
        else:
            print('请输入：是/否')
    if jiez == '是':
        user_ca = {}  # 读取文件中的信息，将信用卡卡号的信息放入字典
        user_pw = {}
        user_yue = {}
        with open('xinyongka.txt', 'r', encoding='gbk')as f:
            for line in f:
                line_list = line.replace('\n', '').split(' ')
                user_ca[line_list[0][:4]] = int(line_list[0][5:])
                user_pw[line_list[4][:4]] = int(line_list[4][5:])
                user_yue[line_list[2][:3]] = int(line_list[2][4:])
        while True:
            tix_card = int(input('请输入信用卡号：'))
            tix_pswd = int(input('请输入信用卡密码：'))
            if tix_pswd != user_pw['pwsd'] or tix_card != user_ca['card']:
                print('用户名或密码错误，请重新输入')
                continue
            else:
                print('信用卡账号密码登录成功！请继续支付：')
                user_shop = {}
                with open('shop.txt','r',encoding='utf-8')as f:
                    for line in f:
                        line_list = line.replace('\n', '').split(' ')
                        user_shop[line_list[0][:4]] = int(line_list[0][5:])
                if user_yue['yue']>=user_shop['sale']:
                    res = user_shop['sale']
                    print('支付成功!本次支付金额为%s元。'%res)
                else:
                    print('余额不足，支付失败')
                    #continue
            break