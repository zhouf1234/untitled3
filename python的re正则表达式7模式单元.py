import re

#模式单元
match = re.match('\w{3}\d{2}hello','a_c22hello') #\w匹配三个,\d匹配两个
print(match)

match = re.match('\w{3}\d{2}hello','b2d55hello')#\w匹配三个,\d匹配两个
print(match)

match = re.match('(\w{3}\d){2}hello', 'abc9a_c8hello')
print(match)
print()

# 暂存内容
match = re.match('h(e)l(l)(o)', 'hello world')
print(match)
print(match.groups())  # 空元组

print()
url = 'https://www.shibi.com/product/12323.html'
pattern = '([a-zA-Z]+)://(\w+(?:\.\w+){2,3})(.+)'
match = re.match(pattern, url)

print(match)
print(match.groups())
