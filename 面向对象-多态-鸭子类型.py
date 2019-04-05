# 多态例：鸭子类型
# 鸭子类型：python作为动态类型语言，无法指定参数(usb_obj)类型
# 多态应用时，作为参数的参数的对象即使不是要求的类型，只要有相应的方法(run)，也可正常执行xiyiji

#定义一个插口类
class Usb:
    def run(self):
        pass

class Udist(Usb):
    def run(self):
        print('u盘在运行...')

class Mouse(Usb):
    def run(self):
        print('鼠标在运行...')

class Keyborad(Usb):
    def run(self):
        print('键盘在运行...')

class Xiyiji(Usb):
    def run(self):
        print('洗衣机在运行。。。')

#实例化 U盘，鼠标，键盘
ud=Udist()
um=Mouse()
uk=Keyborad()
# 实例化
ux=Xiyiji()


#定义电脑类：
class Computer():
    #使用usb插口,传的run的方法
    def useUsb(self,usb_obj):
        usb_obj.run()

#实例化一个电脑
c=Computer()
c.useUsb(ud)    #显示U盘在运行。。。
c.useUsb(um)    #鼠标在运行。。。
c.useUsb(uk)    #键盘在运行。。。

c.useUsb(ux)
