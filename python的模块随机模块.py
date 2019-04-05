#随机模块：random 模块
import random

print(random.random())                   #(0,1)----float    大于0且小于1之间的随机小数
print(random.randint(1,10))              #[1,10]    大于等于1且小于等于10之间的随机整数
print(random.randrange(1,10))             #[1,10)    大于等于1且小于10之间的随机整数

print(random.choice([1,'23',[4,5],'hello']))    #从一个列表取出1或者23或者[4,5]的随机元素
print(random.sample(['hello', 100, 200, [1,2,3]], 3))    # 随机从列表中取出 指定个数的参数
print(random.uniform(1,3))               #大于等于1小于3的小数，如1.927109612082716
print()

#打乱列表
L = [i for i in range(1,20)]
print(L)
random.shuffle(L)
print(L)