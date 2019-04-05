#定义函数
#num1  和 num2就是参数
#num1 就是形参
#形参本质上就是变量，变量的值就是函数调用时给的实参

def add_num(num1,num2):
    return num1 +num2
#调用函数
print(add_num(2,6))     #显示8。   2、6是实参
print(add_num(20,30))     #显示50。20，30是实参

#如果函数调用时，实参的数量少了,会报错
#如果函数调用时，实参的数量多了,也会报错
#add_num(100)
#add_num(2,4,6)