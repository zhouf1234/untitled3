#用于有序的数据类型：list  tuple  str
#写法理解（开始：结束：step）
#数组例
boy_firends = ['李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦']

print(boy_firends[3])  #按下标取出其中一个元素
print(boy_firends[2:5]) #取出2到4的元素
print(boy_firends[0:4]) #取出前四个元素
print(boy_firends[:4])  #取出前四个元素
print(boy_firends[1:6:2])#取第1个到第6个，中间各2个
print(boy_firends[:6:2])#从0开始到6，中间各2个
print()

print(boy_firends[-3])         #倒数第三个
print(boy_firends[2:-5])      #正2倒5
print(boy_firends[-1:-4:-1])  #最后三个
print(boy_firends[:-4:-1])     #最后三个
print(boy_firends[:-4])       #倒数第四个一直倒数最后
print()

print(boy_firends[-1::-1])  #反转列表
print(boy_firends[::-1])    #反转列表
print(boy_firends[::])     #复制列表，变成一个新的
print(boy_firends[::2])   #取列表中的，中间各两个
print(boy_firends[::-2])  #倒取列表中的，中间各两个

print(boy_firends[3:])    #从第三个一直到结束
print(boy_firends[3:-1]) #从第三个一直到倒数第一个结束
print()

msg = 'hello dandan'
print(msg[:-4:-1])
print(msg[3:])

