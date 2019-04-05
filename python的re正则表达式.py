import re

input_content = input('>>>')           #输入要验证的字符串
#match：从字符串开头开始匹配
print(re.search('hello',input_content))  #判断输入的有没有hello，有的话，下标在哪几位
print(re.match('\d+',input_content))  #判断输入的是不是数字，不是就none；有的话，下标在哪几位
print(re.match('h',input_content))   #判断输入的是不是字母h
print(re.match('\u4e00',input_content))#判断输入的是不是汉字一
print(re.match('好',input_content))#判断输入的是不是汉字好
print()

#字符类
print(re.match('[abc]',input_content))   #判断输入的是不是字符a，b，c或它们的组合
print(re.match('[^abc]',input_content))#判断输入字符串是不是字符a，b，c作为开头
print(re.match('[0-9]', input_content))     #判断输入的是不是包含1-9
print(re.match('[a-z]', input_content))      #判断输入的是不是包含a-z
print(re.match('[A-Z]', input_content))      #判断输入的是不是包含A-Z
print(re.match('[A-D]', input_content))      #判断输入的是不是包含A-D
print(re.match('[你我a2]', input_content))
print(re.match('[a-zA-Z0-9]', input_content))
print(re.match('[!-=]', input_content))
print(re.match('[^a-zA-Z]', input_content))
print()


print(re.match('\d', input_content))  # [0-9]
print(re.match('\D', input_content))  # [^0-9]
print(re.match('\w', input_content))  # [0-9a-zA-Z_]
print(re.match('\W', input_content))  # [^0-9a-zA-Z_]
print(re.match('\s', input_content))  # [\n\t\v\f\r] 所有空白字符
print(re.match('\S', input_content))  # [^\n\t\v\f\r] 除了空白字符