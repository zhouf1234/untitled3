#打开两个文件，把一个文件的内容写入到另一个文件中:方法1
#wf = open('文件2.txt','w')
#rf = open('文件例.txt','r')
#wf.write(rf.read())

#wf.close()
#rf.close()

#打开两个文件，把一个文件的内容写入到另一个文件中:方法2更常用
with open('文件例.txt', 'r') as rf, open('文件2.txt', 'w') as wf:
    wf.write(rf.read())



