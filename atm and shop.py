import ashop1,ashop2,atm5

def foo():
    ashop1.shop_one()            #加入购物车
    ashop2.shop_two()
def bar():
    atm5.atm_q()                   #atm用户入口

fn_dict ={
    'shopping':foo,
    'atm':bar
}
#获取输入
choise = input('请选择shopping/atm：')
fn_dict[choise]()