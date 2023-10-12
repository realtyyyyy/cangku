import scrapy


class DangdangSpiderSpider(scrapy.Spider):
    name = "dangdang_spider"
    allowed_domains = ["dangdang.com"]
    start_urls = ["https://dangdang.com"]

    def parse(self, response):
        pass
