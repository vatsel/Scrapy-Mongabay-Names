# -*- coding: utf-8 -*-

# Scrapy settings for names project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'names'
CONCURRENT_REQUESTS=1
DOWNLOAD_DELAY=1
ITEM_PIPELINES = {
    'names.pipelines.RankedNamesPipeline' : 300
}
NEWSPIDER_MODULE = 'names.spiders'
SPIDER_MODULES = ['names.spiders']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'names (+http://www.yourdomain.com)'
