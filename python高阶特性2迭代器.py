from collections.abc import Iterator


L = [10,20,30,40]
map_L = map(lambda x:x+1, L)

print(map_L)  #迭代器

print(next(map_L))
print(next(map_L))
print(next(map_L))
print(next(map_L))
# print(next(map_L))   #没了就报错

#f = open('文件4.txt', 'r', encoding='utf-8')
#print(next(f))

# print(next(f))

#print()
print(isinstance({}, Iterator))
#print(isinstance(f, Iterator))
print(isinstance(map_L, Iterator))
