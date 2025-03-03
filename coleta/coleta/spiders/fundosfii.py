import scrapy


class FundosfiiSpider(scrapy.Spider):
    name = "fundosfii"
    allowed_domains = ["www.fundsexplorer.com.br"]
    start_urls = ["https://www.fundsexplorer.com.br/ranking"]

    def parse(self, response):
        pass
