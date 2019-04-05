class Open:
    def __enter__(self):
       return 100

    #with执行结束时调用,可以获取with内部错误信息（此次是print(o.name)）
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('执行完了')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True         #写了此条。写啥（比如下方故意写错的print(o.name)）都不报错（除了语法错误）

with Open() as o:
    print(o)            #100
    print()
    print(o.name)       #name不存在，故意写错验证def __exit__