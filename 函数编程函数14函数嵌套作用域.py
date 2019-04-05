def fn01():
    name = 'xiao'
    def fn02():
        age = 19
        print(name)
        def fn03():
            print(name)
            add = '上海'
            print(age)
            #print(add)可用
        fn03()
        #print(add)不可用
    def fn03():
        phone = '123123123'
    fn02()
    fn03()
fn01()               #输出xiao  xiao   19三行，name,age,add都是局部变量