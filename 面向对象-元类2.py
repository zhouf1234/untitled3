#type来构建一个类
Person=type('person',(object,),{'name':'dada','age':16})

#实例化元类
p=Person()
print(Person)
print(p)
print(p.name)
print(p.age)