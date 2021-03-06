#用户名和密码存放于文件中，格式为：admin|123456

msg_dic = {     #一个商品列表
    '101':{'name':'apple','sale':10},
    '102':{'name':'mac','sale':10000},
    '103':{'name':'xiaomi','sale':600},
    '104':{'name':'lenovo','sale':3000},
 }

name = input('用户名:')
pwd = input('密码:')
with open('file-one.txt','a',encoding = 'gbk') as f:
    f.write('%s |%s \n' %(name,pwd))

#登录
for y in range(0,3):
    names = input('输入用户名:')
    pasds = input('输入密码:')
    list = []
    with open('file-one.txt', 'r', encoding='gbk') as f:
        for i in f:
            list = i
    if pasds not in list or names not in list:
        print('用户名或密码错误,还有%d次机会' % (2 - y))
        continue
    print('登录成功！')
    break
    # 输入工资并打印商品列表

gongzi = int(input('请输入您的工资：'))
shop_list = {}
while True:
    print('商品信息')
    for key, msg in msg_dic.items():  # items将key和value一起遍历出来
        print('商品ID：%s  商品名：%s  商品价格：%s' % (key, msg['name'], msg['sale']))
    id = input('请输入商品id：')
    if id == 'quit':             # 判断用户输入:结束和重新输入设置
        break
    if id not in msg_dic:
        print('重新选择：')
        continue
    if id in shop_list:             # 添加购物车
        shop_list[id]['num'] += 1
    else:
        shop_list[id] = {           # 在购物车里面添加信息
                'name': msg_dic[id]['name'],
                'sale': msg_dic[id]['sale'],
                'num': 1
            }
    print('商品已添加到购物车，请选择退出 (输入quit) 还是继续购物(enter键)')
    choise = input('>>>:')
    if choise == 'quit':
        break

print('----------购物车---------')
for key, goods in shop_list.items():
    print('商品ID：%s  商品名：%s  商品价格：%s 商品数量：%s' % (key, goods['name'], goods['sale'], goods['num']))
res = 0                             #判断余额
yue = 0
for key, shop in shop_list.items():
    res += shop['sale']
    yue = gongzi - res
if yue>=0:
    print('请付款')
    print('您的余额:%s'%yue)
else:
    print('余额不足')
