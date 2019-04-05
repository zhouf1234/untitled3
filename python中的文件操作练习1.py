# 模拟登陆的， 可以注册  注册完成后 用户名密码写入到文件中。
# 登陆的时候验证的用户名密码来自于 文件 登陆成功 进入程序      :需要改进
name = input('users:')
pasd = input('psd:')
with open('file2.txt','w',encoding = 'gbk') as f:
    f.writelines('name:%s     pasd:%s' %(name,pasd))

    names = input('用户名:')
    pasds = input('密码:')
with open('file2.txt','r') as f:
     data = f.read()
if pasds  in data and names  in data:
    print('ok')
else:
    print('not')


