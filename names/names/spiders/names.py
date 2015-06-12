# -*- coding: utf-8 -*-
import scrapy
from names.items import RankedNameItem
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy import log


class MongabayRankedFirstNamesSpider(CrawlSpider):
    name = "mongabay_ranked_fnames"
    allowed_domains = ["mongabay.com"]
    start_urls = [
        'http://names.mongabay.com/male_names_alpha.htm',
        'http://names.mongabay.com/female_names_alpha.htm'
    ]

    def parse(self, response):
        items = []
        nameRows = response.xpath('//table[@id="table1"]//tr[position()>1]')
        for nameRow in nameRows:
            item = RankedNameItem()
            item['name'] = unicode.title(nameRow.xpath('td[1]/text()').extract()[0])
            item['rank'] = nameRow.xpath('td[4]/text()').extract()[0]
            items.append(item)            
        return items
    
class MongabayLastRankedNamesSpider(CrawlSpider):
    name = "mongabay_ranked_last_names"
    allowed_domains = ["names.mongabay.com"]
    start_urls = ['http://names.mongabay.com/data/surnames_A.htm']    
    rules = [Rule(LxmlLinkExtractor(allow='/surnames_',allow_domains=allowed_domains),callback='parse_item')]
    
    def parse_item(self, response):
        items = []
        nameRows = response.xpath('//table[@style="table1"]/tr[position()>1]')
        for nameRow in nameRows:
            item = RankedNameItem()
            item['name'] = unicode.title(nameRow.xpath('td[position()=1]/a/text()').extract()[0])
            item['rank'] = nameRow.xpath('td[position()=2]/text()').extract()[0]
            items.append(item)            
        return items 
