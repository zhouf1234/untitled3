#进程休眠（延迟）
import time

#print(time.clock())#以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

print('hello')
time.sleep(3)  #3秒延迟后输出后面的print
print('coco')
print()


print(time.altzone)