import re

input_me = input('请输入邮箱/qq/邮编/座机号码/身份证号：')
#1. 要用户输入邮箱，判断是否是邮箱
print(re.match('\w*@\w*\.\w{2,3}',input_me))

#要用户输入QQ号，判断是否是QQ号
print(re.match('\d{8,10}$',input_me))

##3. 要用户输入邮编，验证是否是邮编
print(re.match('\d{6}$',input_me))

#4. 要用户输入座机号码，验证座机号
print(re.match('0\d{2,3}\-\d{7,8}$',input_me))

#5. 验证身份证号
print(re.match('\d{6}(1|2)(8|9|0)\d{2}(0|1)\d(0|1|2|3)\d{4}(\d|x)$',input_me))

