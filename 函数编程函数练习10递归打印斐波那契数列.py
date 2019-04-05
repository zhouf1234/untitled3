#13、 使用递归打印斐波那契数列(前两个数的和得到第三个数，如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, )
def fn(a,y):
    print(a)
    x=a+y
    if x<100:
        return fn(y,x)
print(fn(0,1))
print()

def seq(n):                    #第二种方法，解题
    '''
    params：要求的数列长度
    :return: 一个列表
    '''
    #递归的结束条件：
    if n <= 1:
        return [0]
    if n <= 2:
        return [0,1]
    #获取前面的数列：
    pre_list = seq(n-1)                               #获取前面的列表
    last_index = len(pre_list)-1                       #获取最后一个数字的索引
    curr = pre_list[last_index]+pre_list[last_index-1]  #计算当前的数字，
    pre_list.append(curr)                               #把当前的数字加入列表
    return pre_list                                    #返回加入了当前数字的列表
print(seq(10))
