#队列：先进先出
#堆栈：先进后出

#队列:删除最先添加的
users = []
users.append('a')   #append:直接给列表后添加元素
users.append('b')
users.append('c')
users.append('d')
users.append('abc')
print(users)
users.pop(0)
print(users)
print()

#堆栈:先删除最后面添加的
usersi = []
usersi.append('e')   #append:直接给列表后添加元素
usersi.append('f')
usersi.append('g')
usersi.append('h')
usersi.append('ijk')
print(usersi)
usersi.pop()
print(usersi)
print()