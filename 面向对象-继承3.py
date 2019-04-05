#类继承应用例

class Hero:
    def __init__(self,nickname):
        self.nickname=nickname
        self.agg=0
        self.life_value=0
        self.arrom=0

    def left_move(self):
        print('%s向左移动'%self.nickname)

    def right_move(self):
        print('%s向右移动'%self.nickname)

    def up_move(self):
        print('%s向上移动' % self.nickname)

    def down_move(self):
        print('%s向下移动' % self.nickname)


    def attach(self,obj):
        obj.life_value -= self.agg-obj.arrom

# 如果继承类的时候没有nickname，则和nickname相关的都没有了
#
class Rviwen(Hero):
    def __init__(self,nickname):
        # self.nickname=nickname   #也可，里面有多个参数时，尽量多用 Hero.__init__(self,nickname)这个方法
        Hero.__init__(self,nickname)
        self.agg=12
        self.life_value=56
        self.arrom=2

class Gailun(Hero):
    def __init__(self,nickname):
        # self.nickname = nickname
        Hero.__init__(self,nickname)
        self.agg=14
        self.life_value=58
        self.arrom=3

r=Rviwen('anan')
g=Gailun('bobo')

r.left_move()
g.down_move()
g.right_move()