#定义字符串
s1 = "nihao!"
s2 = 'woyeshi.'     #单引号和双引号都可
print(type(s1),type(s2))
print(s1,s2)

#多行字符串:三种输出方式
shi = '草,\n离离原上草，\n一岁一枯荣，\n野火烧不尽，\n春风吹又生.'  #\n换行符
print(shi)

shi2 = """
    草；
    离离原上草；
    一岁一枯荣；
    野火烧不尽；
    春风吹又生。
"""
print(shi2)

shi3 = '''
    草；
    离离原上草；
    一岁一枯荣；
    野火烧不尽；
    春风吹又生。
'''
print(shi3)
print()

#字符串运算
msg = 'dandan'
print(msg + '100')
print(msg * 5)
print(3 * msg)
#取字符串中某个字符串：按其下标(index)索引，从0开始
print(msg[1])
print()

message = 'a \\ b‘\cd'
print(message)
