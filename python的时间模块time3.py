import time#结构化时间

t = time.localtime()
print(t)
print(type(t))

print(isinstance(t, time.struct_time))
print(isinstance(t, tuple))
