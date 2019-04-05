class Stu:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __getattr__(self, item):
        # _stu是拼接的类名
        return self.__dict__['_Stu'+item]

    def __setattr__(self, key, value):
        if (not key.startswith('_Stu')):
            key = '_Stu'+key
        self.__dict__[key]=value

s=Stu('xiaoxiao',15)

# 给私有属性重新赋值
s.__name='草草'


# 获取私有属性的值
print(s.__name)
print(s.__age)


print(s.__dict__)
