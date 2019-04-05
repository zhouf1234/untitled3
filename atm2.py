# 2：每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
#3:给信用卡还款
import time
ti = time.strftime('%d')
print('今天是本月%s日'%ti)
if ti == '12':
    print('今天是还款最后一天,您当月的剩余还款金额为：')
elif ti == '13':
    print('今天是信用卡账单日，请在下月十号之前还清账单')#下一行print当月总的消费金额

while True:
    huank = input('今天是否还款(是/否): ')
    if huank in ['是', '否']:
        break
    else:
        print('请输入：是/否')
if huank == '是':
    user_jine = {}  # 读取文件中的信息，将银行卡金额的信息放入字典
    user_card = {}
    user_pswd = {}
    with open('yinhangka.txt', 'r', encoding='gbk')as f:
         for line in f:
             line_list = line.replace('\n', '').split(' ')
             user_jine[line_list[2][:3]] = int(line_list[2][4:])
             user_card[line_list[0][:4]] = int(line_list[0][5:])
             user_pswd[line_list[4][:4]] = int(line_list[4][5:])
    while True:
        huank_card = int(input('请输入银行卡号：'))
        huank_pswd = int(input('请输入银行卡密码：'))

        if huank_pswd != user_pswd['pwsd'] or huank_card != user_card['card']:
            print('用户名或密码错误，请重新输入')
            continue
        else:
            print('银行卡账号密码登录成功！')
            huank_jin = int(input('请输入您的还款金额：'))
            if huank_jin <=user_jine['yue']:
                print('还款成功')
            else:
                print('余额不足')
        break






