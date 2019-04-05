class Person:
    school='阳光大学'

    def __init__(self):
        self.name='小赵'
        self.age=20


p1=Person()
p2=Person()
p3=Person()
#dict:显示所有实例化属性和值
print(p1.__dict__)
print()

class Animal:
    #给Animal定义了__dict__的属性只能有这三个
    #用以代替__dict__，_dict__就没有用了，__slots__对内存利用效率高
    __slots__ = ['name','age','sex']

    #此处可写add
    add='上海'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        #self.add=lundon  #__slots__已经写了属性，没有add，所以该Animal对象只能有__slots__定义好的属性


a=Animal('anna',29,'女')
print(a.__slots__)

a.age=36

