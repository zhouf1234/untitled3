import os
def get_dir_size1(pathname):
    '''
    :param filename: 目录的路径
    :return: None
    '''
    if os.path.isdir(pathname):              #判断是否是目录
        for file in os.listdir(pathname):    #os.listdir()  返回列表  目录中的子目录和文件
            filename = os.path.join(pathname,file)
            get_dir_size1(filename)
        os.rmdir(pathname)                     #删除目录
    else:
        os.remove(pathname)                    #删除文件
