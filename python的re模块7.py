import re,os
from urllib import request

# 获取网页内容
with request.urlopen('http://desk.zol.com.cn')as f:
    data = f.read()
#解码
html = data.decode('gbk')
#print(html)  #相当于爬虫
## 定义一个匹配图片url 的正则，找出该网站所有图片地址
image_pattern = '<img[^>]*src=[\'"]?(http[^>]+)[\'"]?[^>]*>'
res = re.findall(image_pattern,html,re.I)
#for i in res:
   # print(i)
for url in res:
    filename = os.path.join('./images', os.path.basename(url))
    # 文件复制
    with request.urlopen(url) as rf, open(filename, 'wb') as wf:
        wf.write(rf.read())
    print(filename + '下载完成！')