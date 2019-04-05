def fn(x):             #fn：回调函数
    return x * x

def add(a,b,f):        #add：高阶函数
    return f(a) + f(b)  #调用参数f，同时使a,b作为f的参数;调用fn函数值,返回值即：(a*a)+(b*b),两个fn(x)
#求平方和
print(add(10,2,fn))      #此处fn不加（），加了就变调用fn的返回值，不加（）就是调用函数本身,千万注意
#求绝对值的和
print(add(2,-4,abs))
#把两个数字，像字符串那样拼起来
print(add(34,12,str))

print(str(12312))