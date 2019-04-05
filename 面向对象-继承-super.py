#super:调用父类的方法和属性，其实根据mro列表去调用
# super（）关键字:super(A,self).test()，等同于调用mro列表中下一个类的方法，A为指定类
class DD:
    def test(self):
        print('from DD')


class A(DD):
    def __init__(self):
        super().test()


class B(DD):
    def test(self):
        print('B test')


class C(A, B):
    def test(self):
        print('from C')

    def fn(self):
        #super().test()
        super(C, self).test()
        super(A, self).test()
        super().test() # 等同于 super(C, self)

# 实例化
c = C()
c.fn()
# A.__init__(100)

print(C.mro())