class F:
    def __call__(self):
        print('%s被调用了'%self)
        return 100


#实例化
f=F()
#调用对象，像函数那样
res=f()
print(res)