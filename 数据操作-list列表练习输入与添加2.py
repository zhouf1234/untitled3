#输入一个元素，放入已经存在的列表中,并删除(替换)列表上一个输入的元素,while使之不断循环这个操作
firends = ['李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦']
while True:
    name = [(input('用户名：'))]
    # print(type(name))            #数据类型是list
    firends.extend(name)
    firends.pop(-2)
    print(firends)
print()
