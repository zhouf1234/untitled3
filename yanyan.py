#模块
_name = 'yanyan'
_age = 15
add = 'beijing'

def _demo():
    print('nihao demo')
def _fn():
    print('hello fn')
def get_info():
    print('----get_info----')
    print(_name)
    print(_age)
    print(add)
    _demo()
    _fn()
    print('-----get_info end-----')

if __name__ == '__main__':
    print('啊，我在被做成脚本，直接运行！')
else:
    print('啊，我在被当做模块用!!!!')
