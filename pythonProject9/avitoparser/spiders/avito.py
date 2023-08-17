import scrapy
from scrapy.http import HtmlResponse
from scrapy_selenium import SeleniumRequest

#print('d99')
class AvitoSpider(scrapy.Spider):
    print('d99')
    name = "avito"
    allowed_domains = ["avito.ru"]
    #allowed_domains = ["youla.ru"]
    #allowed_domains = ["hh.ru"]
    #start_urls = ["https://www.hh.ru/"]
    #https://www.avito.ru/nizhniy_novgorod/avtomobili?radius=200&searchRadius=200
    #start_urls = ["https://www.youla.ru/"]

    start_urls = ["https://www.avito.ru/moskva/koshki?cd=1"]

    def start_requests(self):
        print('еее')
        if not self.start_urls and hasattr(self,"start_url"):
            raise AttributeError (
                "Crauling could not start: 'start_urls' not found"
                "or empty (but found 'start_url' attribute instead,"
                "did you miss an 's'?)"
            )

        print('еее')
        for url in self.start_urls:

            yield SeleniumRequest(url=self.start_urls[0])

    #def parse(self, response:HtmlResponse):
        #pass
        #print(response.url)
    def parse(self,response):
        print('dddd')
        links = response.xpath("//a[@class = 'item']/@href").get_all()
        for link in links:
            yield SeleniumRequest(url=link,callback=self.parse_item)

    def parse_item(self, response):
        pass