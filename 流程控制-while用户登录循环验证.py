name='admin'
password='123'

tag=True
while tag:
    inp_name=input('用户名: ')
    inp_pwd=input('密码: ')
    if inp_name == name and inp_pwd == password:
        while tag:
            cmd = input('>>:')

            if cmd == 'quit':
                tag = False
    else:
        print('用户名或密码错误')