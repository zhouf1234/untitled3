# 多态例：

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

#实例化 U盘，鼠标，键盘
ud=Udist()
um=Mouse()
uk=Keyborad()

#多态的意义：一个父类（usb）被多个子类（udist，mouse。。）继承，每个子类重写父类方法，每个子类都有相同方法（run），但每个方法都有各自形态（print）

#定义电脑类：
class Computer():
    #使用usb插口
    def useUsb(self,usb_obj):
        usb_obj.run()

#实例化一个电脑
c=Computer()
c.useUsb(ud)    #显示U盘在运行。。。
c.useUsb(um)    #鼠标在运行。。。
c.useUsb(uk)    #键盘在运行。。。
