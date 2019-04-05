import shelve
#shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;
#key必须为字符串，而值可以是python所支持的数据类型

she = shelve.open('./content')           #下面两行生成的文件名和路径

#she['name'] = '丹丹'                    #这两行直接运行会生成文件，包含其内容丹丹和10，20，30，40，50
#she['data-list'] = [10, 20, 30, 40, 50]

print(she['name'])
print(she['data-list'])
print(she)

she.close()


