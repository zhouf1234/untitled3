class Stu:

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __delitem__(self, key):
        del self.__dict__[key]

s=Stu()

# 像字典那样，给对象添加属性
s['name']='nana'
print(s.name)
print(s.__dict__)
print()
# 像列表字典那样使用要写上魔术方法def __getitem__(self, item):
print(s['name'])

# 像列表字典那样删除
del s['name']
print(s.__dict__)

s[1] = 100
print(s[1])
