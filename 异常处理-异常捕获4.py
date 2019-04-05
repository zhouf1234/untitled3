#凭空抛出一个错误
# raise TypeError('错误。。。')
#raise 100
try:
    raise Exception('异常了')
except Exception as e:
    print(e)
