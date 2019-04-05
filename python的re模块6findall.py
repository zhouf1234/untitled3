import re

#re.finditer和re.findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
mes = 'hello anan How are you? jojo'

pattern = r'\b\w+\b'  #字符串边界\b
print(re.match(pattern,mes).group())
print(re.search(pattern,mes).group())
res = re.finditer(pattern,mes)
for i in res:
    print(i.group())

print(re.findall(pattern, mes))