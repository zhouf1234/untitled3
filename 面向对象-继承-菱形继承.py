#菱形继承，MRO列表
# 子类按顺序从父类继承属性（方法）
class A:
    def test(self):
        print('a')

class B(A):
    # def test(self):
    #     print('b')
    pass

class C(A):
    def test(self):
        print('c')


class D(B):
    def test(self):
        print('D')

class E(C):
    def test(self):
        print('E')

class F(D,E):
    def test(self):
        print('F')


d=F()
d.test()

# 此两条方法可以看到继承顺序（MRO列表）。先F>D>B>E>C>A>object（a在最后，因为a这个父类有俩子类）
# 如果f没有,则继承d，如果d没有，则继承b。。。
print(F.__mro__)
print(F.mro())

"""
(F, D, B, A, E, C, object)
"""