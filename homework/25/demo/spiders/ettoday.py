import scrapy

class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['http://www.ettoday.net/']

    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm',
                  'https://www.ettoday.net/news/20201009/1826868.htm']

    def parse(self, response):
        print(response.xpath('//title/text()').get())
        print(response.xpath('//div[@itemprop="articleBody"]//p/text()').getall())
        
