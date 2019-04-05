name = ' danedanA'           #字符串例
print(name.strip() + '|')     #去掉两边空格
print(name.startswith('da'))  #判断是否以da开头
print(name.endswith('A'))     #判断是否以A结尾
print(name.replace('d','p'))  #把变量的值d替换p
print(name.split('d'))        #根据d分割字符串：d就没有了
print(name.upper())           #全变大写
print(name.lower())           #全变小写
print(name[1])                #输出下标为1的第二个字符
print(name[:3])               #输出前三个字符
print(name[-2:])              #输出后两个字符
print(name.find('e'))         #查找并输出e的下标索引
print(name[:-1])               #去掉最后一个字符
print()

data=['alex',49,[1900,3,18]]#数据切片:list例
name = [print(data[0])]
age = print(data[1])
year = print(data[2][0])
month = print(data[2][1])
day = print(data[2][2])
print(type(name))               #赋值给变量，显示list类型,不太理想的方法，无法转换成其他数据类型
print()