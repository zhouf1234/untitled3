import re

#修饰符类似于逻辑或
print(re.search('a|b','a'))
print(re.search('a|b','b'))
print(re.search('abcdef','b'))
print(re.search('abc|def', 'abc'))
print(re.search('abc|def', 'def'))
print(re.search('ab(c|d)ef', 'def'))
print(re.search('ab(c|d)ef', 'abcef'))
print(re.search('ab(c|d)ef', 'abdef'))

#注释
print(re.search('(?#kk)a|b','a'))