def fn(n):
    print(n)
    if n==0:
        print('--------')
        return
    fn(n-1)
    print(n)

fn(3)
'''
过程递归了解 
fn(3)  输出3 fn(2)
    fn(2)  输出2 fn(1)
        fn(1) 输出1 fn(0)
            fn(0) 输出0
            fn(0) 调用结束
        fn(1) 调用结束 输出1
    fn(2)调用结束 输出2
fn(3)调用结束 输出3
'''

#python解释器的内存管理机制为了防止其无限制占用内存，对函数的递归调用做了最大的层级限制(默认1000)
import sys
print(sys.getrecursionlimit())      # 获取当前递归最大深度
sys.setrecursionlimit(10000)        # 设置递归最大深度
print(sys.getrecursionlimit())
