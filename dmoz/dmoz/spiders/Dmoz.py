import scrapy
from scrapy.spider import Spider  
from scrapy.selector import Selector 
from dmoz.items import Demo01Item

class TestdmozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["dmoz.org"]  
    start_urls = [  
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
    ]
    items=[]
  
    def parse(self, response):  
        sel = Selector(response)  
        sites = sel.xpath('//ul[@class="directory-url"]/li')  
        for site in sites:
            item=Demo01Item()
            item['title'] = site.xpath('a/text()').extract()  
            item['link'] = site.xpath('a/@href').extract()  
            item['description'] = site.xpath('text()').extract()  
            print item['title'],item['link']
            #items.append(item)
            yield item
        #return items
           # print description
