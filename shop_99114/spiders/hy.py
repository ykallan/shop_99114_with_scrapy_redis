# -*- coding: utf-8 -*-
import scrapy
from ..items import Shop99114Item
from scrapy_redis.spiders import RedisSpider


class HySpider(RedisSpider):
    name = 'hy'
    allowed_domains = ['99114.com']
    # start_urls = ['http://shop.99114.com/']
    redis_key = 'start_rul'

    def parse(self, response):
        letters = response.xpath('//div[@class="all_num"]/a/@href').getall()
        for letter in letters:
            # print(letter)
            yield scrapy.Request(url=letter, callback=self.parse_letters)

        locs = response.xpath('//td[@class="td_p"]/a/@href').getall()
        for loc in locs:
            # print('loc', loc)
            yield scrapy.Request(url=loc, callback=self.parse_locs)

    def parse_letters(self, response):
        com_lists = response.xpath('//ul[@class="cony_div"]/li/a/@href').getall()
        for com in com_lists:
            yield scrapy.Request(url=com + '/ch6', callback=self.parse_detail)

        next_pages = response.xpath('//div[@class="page_list"]/a/@href').getall()
        for next_page in next_pages:
            yield scrapy.Request(url=next_page, callback=self.parse_letters)

    def parse_locs(self, response):
        com_lists = response.xpath('//ul[@class="cony_div"]/li/a/@href').getall()
        for com in com_lists:
            yield scrapy.Request(url=com + '/ch6', callback=self.parse_detail)

        next_pages = response.xpath('//div[@class="page_list"]/a/@href').getall()
        for next_page in next_pages:
            yield scrapy.Request(url=next_page, callback=self.parse_locs)

    def parse_detail(self, response):

        com_name = response.xpath('//p[@class="companyname"]/span/a/text()').get().strip()
        cont_name = response.xpath('//div[@class="sj-line sjDiv2"]/p[1]/span[2]/i/text()').get().strip()
        jingyingmoshi = response.xpath('//div[@class="sj-line sjDiv2"]/p[2]/span[2]/text()').get().strip()
        zhuyingyewu = response.xpath('//div[@class="sj-line sjDiv2"]/p[3]/span[2]/text()').get().strip()
        loc = response.xpath('//div[@class="sj-line sjDiv2"]/p[4]/span[2]/text()').get()
        mobile = response.xpath('//li[@class="picContact clearfix"]/div/p[2]/span[2]/text()').get().strip()
        dianhua = response.xpath('//li[@class="addIntroW"]/div[1]/div[1]/ul/li[1]/span[2]/text()').get().strip()
        chuanzhen = response.xpath('//li[@class="addIntroW"]/div[1]/div[1]/ul/li[2]/span[2]/text()').get().strip()
        youxiang = response.xpath('//li[@class="addIntroW"]/div[1]/div[1]/ul/li[3]/span[2]/text()').get().strip()
        address = response.xpath('//li[@class="addIntroW"]/div[1]/div[1]/ul/li[4]/span[2]/text()').get().strip()

        item = Shop99114Item()
        item['com_name'] = com_name
        item['cont_name'] = cont_name.replace('\xa0', '')
        item['jingyingmoshi'] = jingyingmoshi
        item['zhuyingyewu'] = zhuyingyewu
        item['loc'] = loc
        item['mobile'] = mobile
        item['dianhua'] = dianhua
        item['chuanzhen'] = chuanzhen
        item['youxiang'] = youxiang
        item['address'] = address

        yield item
