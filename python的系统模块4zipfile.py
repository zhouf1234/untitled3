import zipfile  #用于压缩和解压缩

#压缩  ：w
zip = zipfile.ZipFile('./data.zip','w')       #压缩包名data，放在当前目录下
zip.write('./data')             #当前目录下的data目录放入压缩包，空目录有点问题
zip.write('./02.txt')           #当前目录下的02.txt放入压缩包，可以写多行，txt文件没有问题
zip.close()

#解压缩：r
z = zipfile.ZipFile('./data.zip','r')      #压缩文件的路径
z.extractall(path='./data3')     #解压到当前目录下的data3文件夹中
z.close()
