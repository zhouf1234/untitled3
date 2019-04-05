class Animal:
    name='animal'

class Cat(Animal):
    pass

class Dog(Animal):
    name='dog'

class SamllDog(Dog):
    pass

sd=SamllDog()


print(sd.name)
print(object)

class Person(object):
    pass


print(object.__dict__)