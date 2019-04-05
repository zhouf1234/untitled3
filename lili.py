#这个模块是lili
user = 'lili'
add = '上海'
name= '我是理理'

def lili_fn():
    print('我是函数lili_fn')
def lili_info():
    print('我的名字是%s，我住在%s' %(user,add))

# 控制 from 模块 import * 导出的变量
__all__=['lili_fn','lili_info']
