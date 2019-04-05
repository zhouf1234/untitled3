#去除空格
msg = ' dandan very like. '
print(msg)
#去掉空格
print(msg.strip() + '|') #去掉两边空格,strip([可指定字符])
print(msg.lstrip() + '|')#去掉左边空格
print(msg.rstrip() + '|')#去掉右边空格
print()

url = '/path/lesson/01.txt'
print(url)
print(url.lstrip('/') )#去除左边的斜杠
print()

msg = 'dandan'
print(msg.upper())  #大写操作;lower,upper 大小写
print(msg.startswith('a'))  #判断是否以指定字符串开始
print(msg.endswith('n'))   #判断是否以指定字符串结束
print()

#字符串的格式化处理
name = 'dandan'
age = '17'
address = 'beijing'
msg = '一个女孩叫{},今年{},住在{}'

res = msg.format(name,age,address)
res = '一个女孩叫{},今年{},住在{}'.format(name,age,address)
res = '一个女孩叫{2},今年{0},住在{1}'.format(age,address,name)
res = '一个女孩叫{user_name},今年{user_age},住在{user_address}'.format(user_name=name,user_age=age,user_address=address)
print(res)
print()

#用split把字符串分割成列表
name = 'root:x:0:0::/roor:/both/bash'
print(name.split())     #split(一般指定分割符)
print(name.split(':'))
print(name.rsplit(':',3))#把前面三个分割出来，后面的作为整体
print()

#把列表合并成字符串：join：分割符调用join
boy_firends = ['李白','关羽','孙悟空','诸葛亮','刘备','张良','司马懿','韩信','刘邦']
print(','.join(boy_firends))
print('->'.join(boy_firends))
print('打爆'.join(boy_firends))
print(''.join(boy_firends))
print()

#用replace用来替换字符串
msg = '杨过说：我只爱姑姑，挚爱小龙女'
print(msg.replace('杨过','杨二'))#用杨二替换杨过
print(msg.replace('杨过','杨二',1))

#判断字符串是否都是数字组成:isdigit
print(msg.isdigit())

#find查找字符串下标
print(msg.find('姑姑'))  #find等同index()返回字符字符串中第一次出现的位置
print(msg.rfind('爱'))   #rfind等同index()返回字符字符串中最后一次出现的位置

#count统计字符串出现的次数：若没有，不显示返回值0，显示-1
print(msg.count('爱'))
print()

#字符串的大小写处理
msg = 'dadan say:i like flower,i like sky.'
print(msg.capitalize())   #首字母大写
print(msg.swapcase())   #大小写翻转
print(msg.title())      #每个单词首字母大写


