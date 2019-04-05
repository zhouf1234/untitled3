def foo():
    print('你好：lili')
def bar():
    print('你好：dandan')

fn_dict ={
    'lili':foo,
    'dandan':bar
}
#获取输入
choise = input('>>>')
fn_dict[choise]()            #加了（）可以被调用