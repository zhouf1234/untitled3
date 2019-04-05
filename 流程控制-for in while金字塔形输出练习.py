'''
    1         4空格      1个星      1行     规律：共五层循环
   111        3空格      3个星      2行     规律2：星数=2*行数-1
  11111         2空格      7个星    3行
 1111111        1空格      7个星    4行
111111111        0空格      9个星   5行
'''

max_level = 5   #定义层数，如果写其他数，依然按照金字塔形来
#循环
for level in range(1, max_level + 1):   #变量level遍历（1-6）这个迭代对象
    #空格
    for i in range(max_level - level):
        print(' ', end = '')             #在一行中连续打印多个空格
     #星星
    for i in range(2 * level - 1):      #在一行中连续打印多个星星
         print('*', end = '')
    print()