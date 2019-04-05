import re

#re.I使匹配对大小写不敏感
print(re.match('hello','HELLO'))       #none
print(re.match('hello','Hello',re.I))  #re.I使匹配对大小写不敏感,这次匹配了
print()
#re.M多行匹配，影响 ^ 和 $,换行符\n做字符串边界
print(re.search('^\d{4}','hello\n10018\nworld',re.M))#针对多行匹配，影响 ^ 和 $,换行符作为字符串边界
print(re.search('hello$','hello 10018\nworld',re.M))#不写\n就是none
print(re.search('\w+$','hello 10018\nworld',re.M))   #10018,hello后面由空格，world后面没有
print(re.search('\w+$','hello 10018\nworld'))      #world
print()
#re.S使 . 匹配包括换行在内的所有字符
print(re.search('.+','可以\n,你好！hello 10018\nworld'))
print(re.search('.+','可以\n,你好！hello 10018\nworld',re.S))
print()
#re.X该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解,忽略正则中的空格
print(re.search('\w \w','hello 20018'))        #o,2
print(re.search('\w \w','hello 20018',re.X))   #he
print()
#re.A:让 \w, \W, \b, \B, \d, \D, \s and \S 执行纯 ASCII 匹配，而不是全部Unicode匹配
print(re.search('\w','可以'))
print(re.search('\w','可以',re.A))  #none
print(re.search('\w','hello',re.A))
print()


#多个标识符一起使用：
print(re.search('^hello$', 'Hello\nworld', re.I | re.M))


