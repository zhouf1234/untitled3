#3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def daxiao(a,b,*args):
    if len(a)>5:
        print(a)
    elif len(b)>5:
        print(b)
    elif len(args)>5:
        print(args)
    print(a,b,args)

#A=input('输入字符串：')
A='apple'
B=[1,2,3,4,5,6]
C=('李',100,(1,2,3,4))
daxiao(A,B,C)

#第二种方法:返回值：True或者False
def da(c):
    return len(c)>5
print(da([1,2,3,4,5,6]))


