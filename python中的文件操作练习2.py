
# 添加用户信息 (name,age,sex,address,phone)  每添加一条，内容加入到文件中:简略版，未给输入写判断条件
name = input('name:')
age = input('age:')
sex = input('sex:')
address = input('address:')
phone = input('phone:')
sum = ['name:%s  age:%s  sex:%s  address%s  phone:%s'%(name , age , sex , address , phone)]
with open('file3.txt','w',encoding = 'gbk') as f:
    f.writelines(sum)


