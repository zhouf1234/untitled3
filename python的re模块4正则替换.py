import re

#re.sub()替换字符串中的匹配项
msg = 'hello world 你好 333!\n明月光\n小轩窗'
print(msg)
print()

#去除字符串的所有空白字符
s = re.sub('\s','',msg)
print(s)
print()

#把字符串的所有汉字替换为*,并指定替换的字符个数
s = re.sub(r'[\u4e00-\u9fa5]','*',msg,5) #中文字的unicode范围为 /u4e00-/u9fa5
print(s)
print()

#替换指定字符
s = re.sub(r'[好月光窗]','*',msg)  #替换好月光窗为*
print(s)
print()