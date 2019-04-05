# 添加用户信息 (name,age,sex,address,phone)  每添加一条，内容加入到文件中:简略版，未给输入写判断条件

#获取用户输入
name = input('name:')
age = input('age:')
sex = input('sex:')
address = input('address:')
phone = input('phone:')

#添加到文件中
with open('file5.txt','a',encoding = 'gbk') as f:
    f.write('%s |%s |%s |%s |%s \n' %(name,age,sex,address,phone))  #  |:分隔符