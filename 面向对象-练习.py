#一个游戏人物即一个对象，给他定义一个类
# 游戏案例，对象交互
class Riven:
    def __init__(self,nickname):
        self.nickname=nickname
        self.life_value=414    #基础生命值
        self.aggressivity=54   #攻击力
        self.armor=12           #护甲
    #操作：攻击,每次攻击都减少对方生命值（life_value）
    def attach(self,jole):
        # 敌方生命值=敌方生命值-（小文文的攻击力-敌方护甲），此次攻击了小盖盖13次才把他战胜，每次攻击生命值减少35
        # 即：455=455-（54-19）
        jole.life_value -= (self.aggressivity-jole.armor)
        if jole.life_value <=0:
            print('%s战胜了%s' %(self.nickname,jole.nickname))

    #使用装备
    def use_equ(self,equ):
        self.life_value += equ.life_add_value
        self.aggressivity += equ.agg_add_value


#第二个游戏人物类
class Gaiwen:
    def __init__(self, nickname):
        self.nickname = nickname
        self.life_value = 455  # 基础生命值
        self.aggressivity = 56  # 攻击力
        self.armor = 19  # 护甲

    # 操作
    def attach(self, jole):
        jole.life_value -= (self.aggressivity - jole.armor)
        if jole.life_value <=0:
            print('%s战胜了%s' %(self.nickname,jole.nickname))

#定义装备类
class BlackClear:
    def __init__(self):
        self.life_add_value=100      #增加生命值100
        self.agg_add_value=9        #增加攻击力9



r=Riven('小雯雯')
g=Gaiwen('小盖盖')
b=BlackClear()
#开始攻击
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)

# 给小文文使用了装备，比原先少一次攻击便可战胜小盖盖
r.use_equ(b)

r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)




