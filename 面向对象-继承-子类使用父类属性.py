#super（）关键字
#交通工具
class Vehicle:
    def __init__(self,name,speed,power):
        self.name=name
        self.speed=speed
        self.power=power

    def run(self):
        print('开动了。。。')

#定义地铁
class Subway(Vehicle):
    def __init__(self,name,speed,power,line):
        # Vehicle.__init__(self,name,speed,power)
        super().__init__(name, speed, power)
        self.line=line

    def run(self):
        print('欢迎乘坐%s %s,速度：%s，马力：%s'%(self.line,self.name,self.speed,self.power))
        # Vehicle.run(self)
        # super() 等同于 super(本类, self) 调用mro列表中下一个类的方法  super(指定类,self)
        super().run()

s=Subway('11号线','400h/m',600,'上海地铁')
s.run()