class A:
    def fn(self):
        print('from A')

class B(A):
    # def fn(self):
    #     print('from B')
    pass

class C():
    # def fn(self):
    #     print('from C')
    pass

class D(B):
    # def fn(self):
    #     print('form D')
    pass

class E(C):
    # def fn(self):
    #     print('from E')
    pass


class F(D,E):
    # def fn(self):
    #     print('from F')
    pass


f = F()

print(isinstance(f, F))
print(isinstance(f, D))
print(isinstance(f, A))
print(isinstance(f, object))
print(isinstance(f, int))
print()

print(issubclass(F, D))
print(issubclass(F, A))
print(issubclass(A, D))
print()

print(F.__bases__)
print(F.__base__)
