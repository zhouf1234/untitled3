chengji = int(input('请输入你的成绩')) #可写成score = float(input('请输入你的成绩'))
#获取用户输入的成绩，并判断成绩的情况
if chengji>=90:                        #可写成 if score >= 90:
    print('优秀')
elif chengji>=80 and chengji<90:       #可写成elif score>=80：
    print('良好')
elif chengji>=70 and chengji<80:        #可写成if score >= 70:
    print('普通')
else:
    print('较差')