#输入一个元素，放入已经存在的列表中,并删除列表第一个元素；while使之不断循环这个操作

boy_firends = ['李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦']
while True:
    name = [(input('名字：'))]
    # print(type(name))            #数据类型是list
    boy_firends.extend(name)
    boy_firends.pop(0)
    print(boy_firends)
print()


firends = ['李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦']
name =[(input('用户名：'))]
print(name + firends)        #第二种方法往列表添加输入框的元素，与上一个的位置不同
