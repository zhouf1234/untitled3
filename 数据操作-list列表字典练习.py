#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/29

"""
Python全栈X期课前练习2
"""

# 第一题
list1 = [{"num": 1}, {"num": 3}, {"num": 5}, {"num": 7}]

# 如何把上面的列表转换成下面的列表？
list2 = [1, 3, 5, 7]

list_one=[]
for i in list1:
    list_one.append(i["num"])
print(list_one)

print(list(map(lambda key:key["num"],list1)))

# 第二题
list3 = [
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},

    {"name": "egon", "hobby": "喊麦"},
    {"name": "egon", "hobby": "街舞"},
]
# 如何把上面的列表转换成下方的列表？
# Talk is cheap, show me the code.
list4 = [
    {"name": "alex", "hobby_list": ["喝酒", "烫头", "Massage"]},
    {"name": "egon", "hobby_list": ["喊麦", "街舞"]},
]
#第一种方法
list_two={"alex":[],"egon":[]}
for s in list3:
    #print(s["name"])
    if s["name"] == "alex":
        list_two["alex"].append(s["hobby"])
    else:
        list_two["egon"].append(s["hobby"])
print(list_two)

#第二种方法
list_th={"name":[],"hobby_list":[]}
list_fo={"name":[],"hobby_list":[]}
for s in list3:
    if s["name"] == "alex":
        list_th["name"]=(s["name"])
        list_th["hobby_list"].append(s["hobby"])
    else:
        list_fo["name"]=(s["name"])
        list_fo["hobby_list"].append(s["hobby"])
print(list_th)
print(list_fo)
print()

#第三个:练习题答案
list_dict={}
for d in list3:
    #print(d)
    if d["name"] not in list_dict:
        list_dict[d["name"]] = d
        list_dict[d["name"]]["hobby_list"]=[d["hobby"],]
        list_dict[d["name"]].pop("hobby")
    else:
        list_dict[d["name"]]["hobby_list"].append(d["hobby"])
#print(list_dict)
ret = list(list_dict.values())    #values得到字典中所有的值 组成的 类表
print(ret)