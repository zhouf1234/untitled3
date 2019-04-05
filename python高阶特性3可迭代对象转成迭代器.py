from collections .abc import Iterator,Iterable   #导入模板
print(isinstance([],Iterator))             #false   :列表不是迭代器，是可迭代对象
print(isinstance([].__iter__(),Iterator))  #true    ：可迭代对象转成了迭代器
print(isinstance('hello'.__iter__(), Iterator))  #True
print(isinstance(iter({}), Iterator))
print()

f = open('文件4.txt', 'r', encoding='utf-8')
print(isinstance(f, Iterator))
f.__iter__()