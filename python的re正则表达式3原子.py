import re

#  . :匹配任意字符，除了换行符
print(re.match('[abc]','b'))
print(re.match('.','b'))
print(re.match('.','我'))
print(re.match('.','\n'))
print(re.match('.','!'))
print(re.match('.','abc\n'))
print()

#模式单元的原子
print(re.match('hello{5}','helloooooaaa'))  #{5}是为了让后面的o都出来,不写只有hello
print(re.match('(hello){1,5}','hellohellohellohello')) #只能匹配一个或n个hello组合
print()

#特殊原子
#匹配字符串中一个
print(re.match('\.','.'))
print(re.match('\.','b'))
print()

# 匹配 \ 本身
s = '\\'
s = r'\\'


print(len(s))
print(s)
print(re.match('\\\\', s))  #原因是 正则写在字符串中
print(re.match(r'\\', s))
print(re.match(r'\\', s))
print(re.match('\.','.'))

print(len('\\\\'))

print()



S = r'a\nb'  # 字符串不会转义了

print(S)