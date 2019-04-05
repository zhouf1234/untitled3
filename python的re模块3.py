#模式单元使用标识符
import re

match = re.search('([a-z]{5}) \w{5}','Hello world')
print(match)
match = re.search('([a-z]{5}) \w{5}','Hello world',re.I)
print(match)
match = re.search('(?i:[a-z]{5}) \w{5}','Hello world',re.I)
print(match)
print(match.groups()) #加了？:就不会暂存内存了