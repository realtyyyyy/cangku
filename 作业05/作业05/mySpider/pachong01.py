import csv
import requests
from lxml import etree
import sqlite3

# 建立数据库连接
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# 创建数据库表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        actor TEXT,
        information TEXT,
        date TEXT,
        star TEXT,
        evaluate TEXT,
        introduction TEXT
    )
''')

# 写入CSV文件的标题
with open('movie_data_new.csv','w',newline='',encoding='utf-8') as fp:
    writer = csv.writer(fp)
    writer.writerow(('name'))

# 网页抓取部分（保持不变）
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#通过request请求访问网页并获取网页内容
for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath("//ol[@class='grid_view']/li")
    #解析网页内容
    for info in infos:
        name = info.xpath(".//div[@class='info']//div[@class='hd']//a/span[1]/text()")
        # 修改部分：将数据插入数据库
        cursor.execute(
            'INSERT INTO movies (name) VALUES (?)',
            (name)
        )

# 提交并关闭数据库连接
conn.commit()
conn.close()