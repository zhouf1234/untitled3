# 2： 生成4位随机验证码 随机字母和数字
import random
#print(random.sample([1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g'],4))
l = [i for i in range(1,10)]      #列表生成器
#print(l)
m=[chr(i) for i in range(97, 123)] #列表生成器
#print(m)
p=l+m
#print(p)
print(random.sample(p,4))