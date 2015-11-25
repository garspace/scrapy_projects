# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector
from douban.items import DoubanItem

class DoubanbookSpider(scrapy.Spider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://www.douban.com/',
		'http://book.douban.com/tag/'
    )

    def parse(self, response):
		topicDict=[]
		itemDict=[]
		doubanItem=DoubanItem()
		#f=open('douban.txt','w')
		res=response.xpath('//div[@class="article"]/div')
		#for contents in res:
		#content=contents.xpath('div/a/h2/text()').extract()
		re=res.xpath('div/table/tbody/tr/td/a/@href').extract()
		i=0
		for links in re:
			#print links
			
			#self.make_requests_from_url(links).replace(callback=self.parse)
			yield Request(re[i],callback=self.parse_2)
			i=i+1
		#for topic in res.xpath('div/a/h2/text()').extract():
		#	print topic
		#	for lebels in res.xpath('div/table/tbody/tr/td/a/text()').extract():
		#		print lebels
				
			#topicDict.append(topics)
			#for topic in topics:
			#	print topics
			#	titles=contents.xpath('//table[@class="tagCol"]/tbody/tr/td/a/text()').extract()
			#	itemDict.append(titles)
			#	print titles
		#doubanItem['topic']=topicDict
		#doubanItem['item']=itemDict
    def parse_2(self,response):
		re=response.xpath('//div[@id="book"]/dl/dd/div[@class="desc"]/text()').extract()
		for books in re:
			print books