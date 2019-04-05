#2 递归实现目录和文件的复制
import os
def copy_dir(src,dst):
    #处理为绝对路径
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    # 判断是否是目录
    if not os.path.isdir(dst):
        print('目标必须是目录！')
        return False

    #判断src是目录还是文件，递归的结束条件
    if not os.path.isdir(src):
        with open(src,'rb')as r_f,open(os.path.join(dst,os.path.basename(src)),'wb')as w_f:
            w_f.write(r_f.read())
    else:
        dir_name = os.path.basename(src)        #获取具体目录名
        os.mkdir(os.path.join(dst,dir_name))    #在目录目录中，创建新的目录
        for file in os.listdir(src):
            copy_dir(os.path.join(src,file),os.path.join(dst,dir_name))
copy_dir('./data3','D:/')     #作用：把本目录下的data3文件夹，复制到D盘主目录下