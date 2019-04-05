#5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者

def sum(*args):
      print(args[1:8:2])   #输出值奇数位索引

B = [1,2,3,4,5,6,7,8]
sum(*B)

#第二种方法：返回值
def get_odd_element(data):
    res_list = []
    for index,val in enumerate(data):
        if index % 2 != 0:
            res_list.append(val)
    return res_list

print(get_odd_element([10,20,30,40,50,60]))
