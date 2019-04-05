import re

#{n}:前面原子的数量 n次
print(re.match('hhhhh','hhhhhhhhhaaaaa'))  #匹配5个h
print(re.match('h{5}','hhhhhhhhhaaaaa'))   #匹配5个h
print(re.match('hel{5}lo','hellllo'))
print()

#{n,m}:前面原子的数量n次到m次
print(re.match('h{2,6}','h'))
print(re.match('h{2,6}','hh'))
print(re.match('h{2,6}','hhhh'))
print(re.match('h{2,6}','hhhhhh'))
print(re.match('h{2,6}','hhhhhhhhhhhh'))   #依然只匹配6个h

print(re.match('h{2,}', 'hhhhhhhhhh'))
print(re.match('h{2,}', 'hh'))
print(re.match('h{2,}', 'h'))

print()

# ?: 前面原子的数量 0次或 1次 {0,1}
print(re.match('hhh?','hhhhhhhhhhhh'))   #只匹配3个hhh
print(re.match('a?', 'hello'))
print(re.match('a?', 'ahello'))
print(re.match('a?', 'aaaaahello'))

#  + ：  前面原子的数量1次或多次 {1,}
print(re.match('hhh+','hhhhhhhhhhhh'))   #h全匹配了
print(re.match('a+', 'hello'))
print(re.match('a+', 'ahello'))
print(re.match('a+', 'aaaaaaaaaahello'))

#  * ：前面原子的数量0次、1次或多次也就是任意次
print(re.match('hhh*','hhhhhffff'))          #h全匹配了
print(re.match('a*', 'hello'))
print(re.match('a*', 'ahello'))
print(re.match('a*', 'aaaaaaaaaaaaahello'))

print('.*','')
print('.*','abshflopd123')           # .是任意字符，有什么匹配什么
print()

# 正则默认会 尽可能多的匹配  贪婪匹配
print(re.match('o{2,6}', 'ooooooooooooooooooooooooooooooooooo'))
# 在数量修饰的后面加上？ 阻止贪婪匹配 尽可能少的匹配
print(re.match('o{2,6}?', 'ooooooooooooooooooooooooooooooooooo'))

print(re.match('.*?', 'sdfjaksldfjaklsfjladskfjklasjflkadsfjkadsfjlkadsfj'))
print(re.match('.+?', 'sdfjaksldfjaklsfjladskfjklasjflkadsfjkadsfjlkadsfj'))
print(re.match('.??', 'sdfjaksldfjaklsfjladskfjklasjflkadsfjkadsfjlkadsfj'))

