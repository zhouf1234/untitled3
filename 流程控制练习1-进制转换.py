yonghu = int(input('请输入一个数字'))
print(bin(yonghu))     #转为二进制

yonghu1 =(input('请输入一个二进制数据'))
#print(type(yonghu1))
print(int(yonghu1,2))


#第二种方法
print('十进制转二进制')
num = int(input('>>>'))
res = bin(num)
print('进制形式:''%s' %res)