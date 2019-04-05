import re
while True:
    #获取用户的输入
    id_name = input('请输入身份证号：')
    #验证身份证格式
    if re.match('^\d{17}[\dxX]$',id_name) == None:
        print('身份证无效')
        continue

     #定义相关数据
    id_xishu = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    id_yushu = ['1','0','x','9','8','7','6','5','4','3','2']
    id_17 = list(id_name[:17])
    id_last = id_name[-1]

    #身份证号每一位与系数相乘，并求和
    sum = 0
    for index,val in enumerate(id_17):
        sum += (int(val) * id_xishu[index])
    #取余数
    check_last = id_yushu[sum % 11]
    # 验证身份证号：
    if check_last.upper() == id_last.upper():
        print('身份证可用')
    else:
        print('身份证无效')
