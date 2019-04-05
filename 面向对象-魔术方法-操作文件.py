#魔术方法操作文件
class File:
    def __init__(self,filename,*,encoding='utf-8'):
        self.__file=open(filename,'r+',encoding=encoding)

    def read(self):
        return self.__file.read()

    def write(self,content):
        self.__file.write(content)

    def __del__(self):
        self.__file.close()

file=File('01.txt',encoding='utf-8')
print(file.read())