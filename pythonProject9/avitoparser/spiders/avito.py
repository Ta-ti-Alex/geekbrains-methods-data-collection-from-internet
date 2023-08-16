import scrapy
from scrapy.http import HtmlResponse


class AvitoSpider(scrapy.Spider):
    name = "avito"
    #allowed_domains = ["avito.ru"]
    #allowed_domains = ["youla.ru"]
    #allowed_domains = ["hh.ru"]
    #start_urls = ["https://www.hh.ru/"]
    #https://www.avito.ru/nizhniy_novgorod/avtomobili?radius=200&searchRadius=200
    #start_urls = ["https://www.youla.ru/"]
    start_urls = ["https://www.avito.ru/nizhniy_novgorod/"]

    def parse(self, response:HtmlResponse):
        #pass
        print(response.url)
