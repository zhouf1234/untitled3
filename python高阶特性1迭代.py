from collections.abc import Iterable


#判断某个数据列席 是否是可迭代的
print(isinstance('hello', Iterable))
print(isinstance(456, Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance({1,3,4}, Iterable))