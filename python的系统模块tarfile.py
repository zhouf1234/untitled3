import tarfile,os

# 压缩
tar = tarfile.open('./dat.tar', 'w')        #压缩包名
for line in os.listdir('./data/03'):        #需要压缩的文件夹/目录
    tar.add(line)

tar.close()


# 解压
tar = tarfile.open('./dat.tar', 'r')
tar.extractall('./data/01')              #将压缩包解压到这个路径
tar.close()