#import scrapy
import scrapy

class NewSpider(scrapy.Spider):
    name = "new_spider"
    starts_url ="http://192.168.80.130/multi"

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@href'
        yield {
            'Image Link':
                x.xpath(newsel).extract_first(),
        }