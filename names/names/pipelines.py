# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pickle, json, os

from scrapy.exceptions import DropItem
from scrapy import log
        
class RankedNamesPipeline(object):
    def __init__(self):
        self.all_names = dict()
        
    def process_item(self, item, spider):
        self.all_names[item['name']]=item['rank']
        return item['name']
        
    def close_spider(self, spider):
        if '' in self.all_names: self.all_names.remove('')
        log.msg("Gathered "+str(len(self.all_names))+" names.",level=log.INFO)
        json.dump(self.all_names,open('namesOut.json',mode='wb'))
