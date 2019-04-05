L = [22,33,6,444,888,222]
print(max(L))  #取得最大值
print(min(L))  #取得最小值

salaries={
    '发哥':3000,
    '铭哥':100000000,
    '丹丹':10000,
    '老朱':2000
}
# 取出工资最高和最低的的人
def salaries_fn(item):
    return salaries[item]

print(min(salaries, key=salaries_fn))   #老朱
print(max(salaries, key=salaries_fn))   #铭哥



