# 实现一个类只能由一个实例，不论多少次实例化，得到的实例还是原先的，对象还是原先的
class Person:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance=super().__new__(cls)
        return cls._instance


p1=Person()
p2=Person()
p3=Person()
p4 = Person()

print(p1 == p2)