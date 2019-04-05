import re

#先行断言（正向预查）：（？=）；用于修饰前面的原子
print(re.search('hello(?=world)','hello world'))  #none
print(re.search('hello(?=world)','helloworld'))  #要求o的后面是world，没有world也是none
print(re.search('hello(?=world)', 'hello'))
print()
#负向先行断言（负向预查）：（？！）；用于修饰前面的原子
print(re.search('hello(?!world)','hello world'))  #要求o后面不是world，没有world也可以
print(re.search('hello(?!world)','helloworld'))   #none
print(re.search('hello(?!world)','hello'))
print()

print(re.search('h(?=hello)hello','hhello'))  #要求h的后面是hello
print(re.search('h(?=hello)hello', 'hhello'))
