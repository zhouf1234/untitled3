#一个字典
goods_list = {
    '101':{'name':'a','sale':1000},
    '102':{'name':'b','sale':2000},
    '103':{'name':'c','sale':2500},
    '104':{'name':'d','sale':3000},
}

shop_list = {}    # 变量 购物车信息
while True:
    for key ,goods in goods_list.items():  #items将key和value一起遍历出来
        print('商品ID：%s   商品名：%s   商品价格：%s' %(key,goods['name'],goods['sale']))

    id = input('请输入商品id：')          #获取用户输入
    if id == 'quit':                      #判断用户输入:结束和重新输入设置
         break
    if id not in goods_list:
        print('重新选择：')
        continue
    if id in shop_list:                   #添加购物车
        shop_list[id]['num'] += 1
    else:
         shop_list[id] = {                   #在购物车里面添加信息
            'name':goods_list[id]['name'],
            'sale':goods_list[id]['sale'],
            'num':1
        }
    print('商品以添加到购物车，请选择退出 (quit) 还是继续购物enter键')
    choise = input('>>>:')
    if choise == 'quit':
        break
#打印购物车信息
print('----------购物车---------')
for key,goods in shop_list.items():
    print('商品ID：%s   商品名：%s   商品价格：%s  商品数量：%s' %(key,goods['name'],goods['sale'],goods['num']))
    print(shop_list)