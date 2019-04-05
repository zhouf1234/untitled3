#1 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，
#输出：['Adam', 'Lisa', 'Bart']：

msg = str(input('输入你的英文名：'))     #输入单个英文名时，即一个字符串
def upper_str(item):
        return item.upper()
def lower_str(i):
        return i.lower()
res = ''.join(list(map(upper_str,(msg[0]))))
res1= ''.join(list(map(lower_str,(msg[1:]))))
print(res+res1)
print()


msg_s = ['adam', 'LISA', 'barT']          #一个列表中的字符串，变为首字母大写，其他小写的规范名字
def upper_st(item):
        return item[0].upper()+item[1:].lower()
print((list(map(upper_st,msg_s))))
print()

#规范的第二种方法，匿名函数方法
L=['adam', 'LISA', 'barT']
l1=list(map(lambda val :val.title(),L))      #title()每个单词首字母大写:字符串操作
print(l1)
