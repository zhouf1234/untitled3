class A:
    pass

class B:
    pass

class C(A):
    pass

#都显示是：<class 'type'>，即元类，类的本身也是类，即元类
print(type(A))
print(type(B))
print(type(C))
print()
print(type(int))
print(type(str))
print()
print(type(type))
print()
print(type(object))