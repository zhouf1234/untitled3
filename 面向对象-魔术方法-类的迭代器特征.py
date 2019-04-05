from collections.abc import Iterator,Iterable
#定义无限的自然数n
class Num:
    def __init__(self):
        self.__num = 0

    def __iter__(self):
        return self

    def __next__(self):
        n = self.__num
        self.__num += 1
        return n

n=Num()
for i in n:
    print(i,'')
    #写个停止条件，不然n就会无限显示下去
    if i >=10:
        break;

print()
print(isinstance(n, Iterable))
print(isinstance(n, Iterator))

