from dir_func import get_dir_size   #调用了dir_func这个py文件的代码，其返回值是文件目录大小
print(get_dir_size('./'))            #返回值是目录文件大小

from dir_fun import get_dir_size1     #调用了dir_fun这个py文件的代码，其返回值是None。要求删除目录
print(get_dir_size1('./dir_fun'))     #此次已经删除了dir_fun这个文件夹，再运行会报错
