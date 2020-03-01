import requests
from lxml import etree
import json

url='https://s.weibo.com/top/summary?cate=realtimehot'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
res=requests.get(url,headers=headers)
root=etree.HTML(res.content)
title=root.xpath("//div[@class='m-wrap']//div[@class='data']//table//tbody//a//text()")
urlm=root.xpath("//div[@class='m-wrap']//div[@class='data']//table//tbody//a/@href")
new_url=['https://s.weibo.com/'+x for x in urlm]
with open('热搜.txt','a')as f:
    for i in range(len(title)):
        f.write('{:}\n地址:{:}\n'.format(title[i],new_url[i]))
