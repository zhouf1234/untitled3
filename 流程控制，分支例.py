#获取用户输出
girl_age = int(input('请输入你的年龄')) #用户输入的都是字符串，要把它变为整型

girl_height= int(input('请输入你的身高：'))  #用户输入的都是字符串，要把它变为整型
girl_weight = int(input('请输入你的体重：')) #用户输入的都是字符串，要把它变为整型
girl_is_beautiful_input= (input('你漂亮吗？yes/no：'))

if girl_is_beautiful_input == 'yes':
    girl_is_beautiful_input = True
else:
    girl_is_beautiful_input = False


#判断，年龄大于18，并且小于60，身高大于140，体重小于220，并且漂亮，就表白
if girl_age>=18 and girl_age<=60 and girl_height>140 and girl_weight<220 and girl_is_beautiful_input == True:
    print('表白')
else:
    print('阿姨好')
