#一个字典
msg_dic = {
'apple': 10,
'tesla': 100000,
'mac': 3000,
'lenovo': 30000,
'chicken': 10,
 }

#购物车变量：
shop_list = []
#循环输出商品：
print('商品信息')
for key in msg_dic:
    print('商品: %s 价格:%s' %(key,msg_dic[key]))

#判断用户选择的商品在不在商品字典中:了解即可
while True:
    chose_good = input('请选择要购买的商品:')
    if chose_good not in msg_dic:           #条件是判断用户输入是否再字典中（成员运算符）
        continue                            #continue  跳出本次循环
    #选择要购买的数量
    count = input('请选择要购买的数量：')
    if not count.isdigit():             #条件是判断是否由数字组成：isdigit
        continue
        #追加到购物车
    shop_list.append((chose_good,msg_dic[chose_good],count))
    print('购物车信息：')
    print(shop_list)





