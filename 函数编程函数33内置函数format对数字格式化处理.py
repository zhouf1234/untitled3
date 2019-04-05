#内置函数format:对数字进行格式化处理
print(format(11,'b'))           #11转换成二进制
print(format(11,'o'))             #11转换成8进制
print(format(11,'x'))              #11转换成16进制 小写字母表示
print(format(11,'X'))             #11转换成16进制 大写字母表示
print(format(11,'f'))              #小数点计数法，默认保留6位小数
print(format(11.111222,'.2f'))        #小数点计数法，指定保留2位小数
print()

# 2e-2  0.01
print()


msg = 'a = 10 + 2'

exec(msg)                  #exec用来执行语句，不会返回任何值
                           #exec把字符串 当代码执行#  没有返回值。 语句  赋值语句 while for if
res = eval('10*3')         #eval用来执行表达式，并返回表达式执行的结果
                           #eval把字符串 当代码还行  执行执行表达式，eval的返回值就是表达式的结果
print(a)                   #12,但是报错
print(res)                  #30

# compile 把字符串当做代码执行
#compile('10 + 20', 'eval')
