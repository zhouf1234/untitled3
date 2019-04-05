
# 一个子类可继承多个父类，如果父类有相同的方法，按顺序
class A:
    def test(self):
        print('a')

class B:
    def test(self):
        print('b')

class C:
    def test(self):
        print('c')

class Dog(A,B,C):
    pass

d=Dog()
d.test()