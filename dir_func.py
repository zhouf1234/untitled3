import os
def get_dir_size(pathname):
    '''
    :param filename: 目录的路径
    :return: 目录的大小
    '''
    if os.path.isdir(pathname):
        total_size = 0
        for file in os.listdir(pathname):
            filename = os.path.join(pathname,file)
            total_size += get_dir_size(filename)
            return total_size
    else:
        return os.path.getsize(pathname)
