# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector

class SspkuSpider(scrapy.Spider):
    name = "sspku"
    allowed_domains = ["ss.pku.edu.cn"]
    start_urls = (
        'http://www.ss.pku.edu.cn/index.php/admission/admbrochure',
    )

    def parse(self, response):
		#print response.body
		sel=Selector(response)
		sites = sel.xpath('//div[@class="info-list"]/ul')
		#print sites
		for site in sites:
			#time= site.xpath('li/a/p[@class.*?left"]/text()').extract()  
			title= site.xpath('li/a/p[@class="info-title"]/text()').extract()  
			link=site.xpath('li/a/@href').extract()
			print ' '*30
			for t in title:
				print t.encode('gb2312')
				print ' '*30
			for i in link:
				print i.encode('gb2312')
			print ' '*30
			#print link.encode('utf-8')