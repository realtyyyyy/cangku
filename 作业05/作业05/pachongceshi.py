import csv
import requests
from lxml import etree

# 打开CSV文件以写入数据
with open('movie_data.csv', 'w', newline='', encoding='utf-8') as fp:
    writer = csv.writer(fp)

    # 先定义要爬取的字段
    writer.writerow(('name'))

    # 定义要爬取的链接及设置header相关参数
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 通过request请求访问网页并获取网页内容
    for url in urls:
        html = requests.get(url, headers=headers)
        selector = etree.HTML(html.text)
        infos = selector.xpath("//ol[@class='grid_view']/li")

        # 解析网页内容
        for info in infos:
            name = info.xpath(".//div[@class='info']//div[@class='hd']//a/span[1]/text()")

            # 将获取的数据写入CSV文件
            writer.writerow((name))