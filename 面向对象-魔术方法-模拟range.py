class Myrange:
    def __init__(self,start,stop):
        self.__start=start
        self.__stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        #不写此两条if语句的话，则会无限显示下去，根本不会管结束字符是谁
        #self.__start即为n的返回值，self.__stop，即为结束字符
        if self.__start == self.__stop:
            #raise StopIteration:合理报错，即效果等同于循环中的break，但迭代器是不能终止的，不能用break
            raise StopIteration
        n= self.__start
        self.__start +=1
        return n


mr=Myrange(10,23)
for i in mr:
    print(i)