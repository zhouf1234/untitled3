#账户间转账：目前只能一个文件的一个账户转另一个文件的账户。。。
user_jine = {}  # 读取文件中的信息，将银行卡的信息放入字典
user_card = {}
user_pswd = {}
with open('yinhangka.txt', 'r', encoding='gbk')as f:
    for line in f:
        line_list = line.replace('\n', '').split(' ')
        user_jine[line_list[2][:3]] = int(line_list[2][4:])
        user_card[line_list[0][:4]] = int(line_list[0][5:])
        user_pswd[line_list[4][:4]] = int(line_list[4][5:])
while True:
    card = int(input('请输入您的银行卡号(只允许输入数字)：'))
    pwsd = int(input('请输入密码(只允许输入数字)：'))
    if pwsd != user_pswd['pwsd'] or card != user_card['card']:
        print('用户名或密码错误，请重新输入')
        continue
    else:
        print('银行卡账号密码登录成功！')
        with open('yinhangkazhuanz.txt', 'r', encoding='gbk')as f:
            data = eval(f.read())
            # for keys,i in data.items():
            # print(keys,i)
            # print('收款人:%s  银行卡号%s' % (keys, i['card']))
        while True:
            zhuan_name = input('请输入收款人名：')
            zhuan_card = int(input('请输入要转账的银行卡号：'))
            if zhuan_name not in data:
                print('账号不存在，请重新输入')
                continue
            if zhuan_card !=data[zhuan_name]['card']:
                print('该银行卡号填写错误！')
                continue
            else:
                print('银行卡账号存在，可以转账！')
                zhuanz_jine = int(input('请输入转账金额：'))
                res = user_jine['yue'] - zhuanz_jine
                print('转账成功！您的余额为:%s' % res)#文件内容没有修改，无法修改文件金额
            break
    break


