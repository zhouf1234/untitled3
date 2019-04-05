menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '黄浦':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闵行':{
            '七宝':{
                '交通大学':{},
                '七宝老街':{}
            },
            '虹桥':{
                '飞机场':{},
                '高铁站':{}
            }
        },
        '闸北':{
            '彭浦新村':{
                '彭浦公园':{}
            },
            '大宁':{
                '灵石公园':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
#打印省、市、县三级菜单，可随时退出程序，如果输入的不在菜单中，则重新选择，可返回上一级菜单选择

#设置遍历保存当前菜单
current_menu = menu
prev_menu = menu
#一级菜单
while True:
    if len (current_menu) == 0:    #菜单下无下拉菜单时，执行的任务
        print('该菜单下已无菜单，可以输入 q 退出')
    #列出菜单
    for key in current_menu:     #遍历current_menu，输出key
        print(key)
    #用户输入
    choise = input('>>>:')
    if choise == 'q':          #如果输入quit，则直接结束循环
        print('byebye!')
        break
    if choise == 'b':
        current_menu = prev_menu
        continue
    if choise not in current_menu:  #如果输入的不在菜单中，则重新选择
        print('请重新选择：')
        continue
    #先把当前menu的值保存下来
    prev_menu = current_menu[choise]
    current_menu = current_menu[choise]# 改变当前的 current_menu





