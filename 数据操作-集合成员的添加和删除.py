#一个集合
boy_firends = {'李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦'}

print(boy_firends)
#集合直接添加一个对象
boy_firends.add('赵云')
print(boy_firends)
#添加多个:和列表(只要是容器都可添加update(Set/List/Tuple) )
boy_firends.update({1,2,3})
boy_firends.update([4,5,6])
print(boy_firends)
#删除集合中的对象
boy_firends.remove('刘备')
print(boy_firends)