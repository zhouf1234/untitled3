# 练习封装后
# 第一个游戏人物类
class Riven:
    def __init__(self,nickname):
        self.__nickname=nickname
        self.__life_value=414    #基础生命值
        self.__aggressivity=54   #攻击力
        self.__armor=12           #护甲

    #封装后，外部无法获取，要用方法取得属性
    def get_nickname(self):
        return self.__nickname

    def get_aggressivity(self):
        return self.__aggressivity
    def set_aggressivity(self,value):
        if value <0:
            print('攻击力不能小于0')
            return
        self.__aggressivity=value

    def get_life_value(self):
        return self.__life_value

    def set_life_value(self,value):
        if value <0:
            print('%s已经失败' %self.get_nickname())
            return
        self.__life_value=value

    def is_die(self):
        if self.get_life_value() < 0:
            print(self.get_nickname() + '已经阵亡')

    def get_armor(self):
        return self.__armor

    #操作：攻击,每次攻击都减少对方生命值（life_value）
    def attach(self, jole):
        jole.set_life_value(self.__aggressivity - jole.get_armor())
        jole.is_die()


    #使用装备
    def use_equipment(self, equipment):
       self.set_life_value(self.get_life_value() + equipment.get_life_add_value())
       self.set_aggressivity(self.get_aggressivity() + equipment.get_aggressivity_add_value())

#第二个游戏人物类
class Gaiwen:
    def __init__(self, nickname):
        self.__nickname=nickname
        self.__life_value=455    #基础生命值
        self.__aggressivity=56   #攻击力
        self.__armor=19

    def get_nickname(self):
        return self.__nickname

    def get_aggressivity(self):
        return self.__aggressivity

    def set_aggressivity(self, value):
        if value < 0:
            print('攻击力不能小于0')
            return
        self.__aggressivity = value

    def get_armor(self):
        return self.__armor

    def get_life_value(self):
        return self.__life_value

    def set_life_value(self, value):
        if value < 0:
            print('%s已经死了' %self.get_nickname())
            return
        self.__life_value = value

    def is_die(self):
        if self.get_life_value() < 0:
            print(self.get_nickname() + '已经阵亡')

    # 攻击
    def attach(self, jole):
        jole.set_life_value(self.__aggressivity - jole.get_armor())


    # 使用装备
    def use_equipment(self, equipment):
       self.set_life_value(self.get_life_value() + equipment.get_life_add_value())
       self.set_aggressivity(self.get_aggressivity() + equipment.get_aggressivity_add_value())


#定义装备类
class BlackCleaver:
    def __init__(self):
        self.__life_add_value = 100
        self.__aggressivity_add_value = 9

    def get_life_add_value(self):
        return self.__life_add_value

    def get_aggressivity_add_value(self):
        return self.__aggressivity_add_value




r=Riven('小雯雯')
g=Gaiwen('小盖盖')
b=BlackCleaver()
#开始攻击
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)

# 给小文文使用了装备，比原先少一次攻击便可战胜小盖盖
r.use_equipment(b)

r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)
r.attach(g)


