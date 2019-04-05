users_year = (input('你是哪一年出生的？'))

shuxiang =((int(users_year) - 1900)%12) + 1

if shuxiang == 1:
    print('属鼠')
elif shuxiang == 2:
    print('属牛')
elif shuxiang == 3:
    print('属虎')
elif shuxiang ==4:
    print('属兔')
elif shuxiang ==5:
    print('属龙')
elif shuxiang ==6:
    print('属蛇')
elif shuxiang ==7:
    print('属马')
elif shuxiang ==8:
    print('属羊')
elif shuxiang ==9:
    print('属猴')
elif shuxiang ==10:
    print('属鸡')
elif shuxiang ==11:
    print('鼠狗')
elif shuxiang ==12:
    print('属猪')
else:
    print('输入错误！')


#第二种方法
"""
2008 鼠     2008%12=4
2009 牛      %12=5
2010 虎      %12=6
2011 兔      %12=7
2012 龙      %12=8
2013 蛇      %12=9
2014 马      %12=10
2015 羊      %12=11
2016 猴      %12=0
2017 鸡      %12=1
2018 狗      %12=2
2019 猪      %12=3
"""
year = int(input('你是哪一年出生的？'))
tag = year % 12
res = ''
if tag == 0:
    res = '猴'
elif tag == 1:
    res = '鸡'
elif tag == 2:
    res = '狗'
elif tag == 3:
    res = '猪'
elif tag == 4:
    res = '鼠'
elif tag == 5:
    res = '牛'
elif tag == 6:
    res = '虎'
elif tag == 7:
    res = '兔'
elif tag == 8:
    res = '龙'
elif tag == 9:
    res = '蛇'
elif tag == 10:
    res = '马'
elif tag == 11:
    res = '羊'

print('你的属相是:'+res)