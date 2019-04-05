import shutil

#文件高级操作:拷贝文件,相当于把01文件的内容直接替换了02的内容
shutil.copyfile('01.txt','02.txt')

#复制文件夹/目录:复制当前的data3文件夹，命名为data2，data2不可存在
#shutil.copytree('./data3','./data2')

#删除文件夹/目录
#shutil.rmtree('./data2')      #此次已经删除

#移动文件夹/目录:02文件夹移动到03文件夹
#shutil.move('./data3/02', './data3/03')  #此次已经移动了

#创建压缩包并返回文件路径；back01：压缩包名，data/01压缩的文件
shutil.make_archive('back01', 'zip', root_dir='./data/01')




