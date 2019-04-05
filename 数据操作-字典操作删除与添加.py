#一个字典
boy_firends = {'name':'李白','age':'17','height':'178','weight':'130'}
print(boy_firends)

#获取其中某一个key的值：
print(boy_firends['age'])

#删除字典成员
del boy_firends['weight']
print(boy_firends)

boy_firends.pop('age')  #返回删除的key对应的值
print(boy_firends)

boy_firends.popitem()  #随机删除字典中的一个（实际上删除最后一个），返回元组（key和value）
print(boy_firends)

boy_firends.clear()
print(boy_firends)     #清空字典
print()

#给字典添加成员：
boy_firends = {'name':'李白','age':'17','height':'178','weight':'130'}

boy_firends['address'] = '夜郎'
boy_firends['firend'] = '杜甫'
print(boy_firends)

#返回指定的key的值：dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
print(boy_firends.get('age'))            #显示17
print(boy_firends['age'])                #显示17
print(boy_firends.get('phone','123456'))  #显示123456
print(boy_firends.get('height','188'))    #显示178

#setdefault 返回指定的key的值方法2:但如果键不存在于字典中，将会添加键并将值设为default
print(boy_firends.setdefault('age'))               #17
print(boy_firends.setdefault('phone',123456789))
print(boy_firends)                                  #123456789被添加进字典了

#判断字典是否为指定的key
print(boy_firends.__contains__('age'))     #显示True
print('name'in boy_firends)                #成员运算符也可，True
print('one'in boy_firends)                #False

#update 添加:dict.update(dict2) 把字典dict2的键/值对更新到dict里
boy_firends.update({'num':100, 'str':'hello', 'name':'武松'})
print(boy_firends)

#快速生成字典
#new_dict = boy_friend.fromkeys('abc')
new_dict = {}.fromkeys(['zhang','li','zhao','qian'], 100)
print(new_dict)



