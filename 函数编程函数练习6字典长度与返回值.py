#6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。字典中的value只能是字符串或列表
#dic = {"k1": "v1v1", "k2": [11,22,33,44]}

def sum(**kwargs):
    for i in kwargs.values():
        if len(i)>2:
            print(i[0:2])

dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
sum(**dic)

#第二种方法：解题
def make_dict(dict_data):
    res_dict = {}
    for key,val in dict_data.items():
        if len(val)>2:
            res_dict[key] = val[:2]
        else:
            res_dict[key]= val[::]
    return res_dict
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
print(make_dict(dic))