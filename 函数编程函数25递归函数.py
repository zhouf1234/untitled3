# 自己调用，自己就是递归函数
#def fn():   没有结束条件的递归，自己无限调用自己
    #print('n')
    #fn()
#fn()

#递归调用要有结束条件
#实现5的阶乘
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
#调用
print(fac(1))
print(fac(5))
print(fac(10))
'''
过程了解递归
fac(5) return 5*fac(4)   5*24=120  此处fac（5）是最后一个完成调用的
    fac(4) return 4*fac(3)   4*6=24
        fac(3) return 3*fac(2)  3*2=6
            fac(2) return 2*fac(1) 2*1=2
                fac(1) return 1
'''

