
age = 17       #设定17
count = 0       #循环变量
while count < 3:        #只允许猜三次
    #获取整型输入
    input_age = int(input('猜年龄：'))
    #进行比较
    if input_age == age:   #==是对比，=是赋值
        print('猜对了')
        break            #猜对就退出循环
    else:
        print('猜错了' '你还有%d次机会' %(2 - count))
    count += 1

#客户猜错3次，但是再给一次机会的话：
    if (count == 3):
        choise = input('再来一次：')
        if choise in ['x','y']:    #如果输入y，就在给用户1次机会
            count = 0               #使次数归0
        else:
            print('游戏结束')




