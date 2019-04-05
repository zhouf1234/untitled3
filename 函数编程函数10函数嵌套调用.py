# 嵌套定义
def fn(num):
    a = num + 100
    def demo():
        print('hello demo')
    demo()
    print('hello fn')
    print(a)

fn(100)          #三个print，输出hello demo ，hello fn，200这三行
# demo() #demo 不能调用
