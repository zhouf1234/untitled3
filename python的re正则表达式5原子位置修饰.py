import re

print(re.match('hello','helloworld'))
print(re.match('hello','nihao hello world'))   #不在开头匹配不到
print()

#单词边界,匹配一个单词边界，也就是指单词和空格间的位置
print(re.match(r'hello\b','hello'))
print(re.match(r'hello\b','hello world'))
print(re.match(r'hello\b','nihao hello world'))  #none：不在开头匹配不到
print(re.match(r'hello\b','helloworld'))         #none：
print(re.match(r'hello\b','nihaohello'))         #none：
print(re.match(r'hello\b','hello,world'))
print(re.match(r'hello\b','hello-world'))
print(re.match(r'hello\b','nihao hello world'))
print()
print(re.search(r'\ber\b', 'layer'))
print(re.search(r'er\b', 'layer'))
print(re.search(r'\ber\b', 'er'))
print(re.search(r'\ber\b', 'hello er'))
print(re.search(r'\Ber', 'hello er'))
print(re.search(r'\Ber', 'layer'))
print(re.search(r'\Ber\B', 'layer'))
print()

#字符串边界
print(re.search('^hello', 'world hello'))
print(re.search('^hello', 'hello world'))
print(re.search('hello$', 'hello world'))
print(re.search('world$', 'hello world'))
print(re.search('^world$', 'hello world'))
print(re.search('^world$', 'world'))

print(re.search('^1[356789]\d{9}$', 'asdf13838385438asdfadsf'))
print(re.search('^1[356789]\d{9}$', '13838385438'))

# re.match() 和 re.search()的区别
print(re.match('hello', 'hello world'))
print(re.search('^hello', 'hello world'))


print(re.search('\Ahello\Z', 'hello'))
