# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Shop99114Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    com_name = scrapy.Field()
    cont_name = scrapy.Field()
    jingyingmoshi = scrapy.Field()
    zhuyingyewu = scrapy.Field()
    loc = scrapy.Field()
    mobile = scrapy.Field()
    dianhua = scrapy.Field()
    chuanzhen = scrapy.Field()
    youxiang = scrapy.Field()
    address = scrapy.Field()
