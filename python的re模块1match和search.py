import re
#match和search
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
#re.search匹配整个字符串，直到找到一个匹配。

match = re.match('(h(e)ll(\w))','hello world hello') #(h(e)ll(\w))是一个模式单元
print(match)
print(match.group())  # gorup匹配的整个表达式的字符串
print(match.group(1))#返回第一个模式单元匹配的内容，数字指定几就是第几个模式单元匹配的内容
print(match.group(2))
print(match.group(3))
print(match.groups()) #返回元组，元组中是匹配到的模式单元的内容，没有模式单元，就空元组
print(match.span())   #返回元组，匹配到的字符串位置（开始，结束）
print(match.start())  #匹配到的字符串开始的位置
print(match.end())   #匹配到的字符串结束的位置
print()

match = re.search(r'\b\w{2,6}\b','hello world hello')
print(match)
print(match.group())