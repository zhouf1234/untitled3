class Person:

    def __init__(self):
        #__两条杠封装属性，使其私有属性，外部无法访问，只能内部访问
        #_school__，不封装，_一条杠也不封装
        self.name='anan'
        self.__age=17
        self._sex='male'
        self._school__='阳光小学'

    def __eat(self):
        print('吃吃吃吃')

p=Person()
print(p.name)
print(p._sex)
print(p._school__)
print()

print(p._Person__age)
p._Person__eat()

print()

print(p.__dict__)