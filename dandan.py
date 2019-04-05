#这是一个模块
name = 'dandan'
age = 18

def read():
    print('我是模块中的read函数')
def get_info():
    print('我的名字是%s，我今年%s岁' %(name,age))
def set_name(value):
    global name
    name = value
print('你用了我的模块')

