# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
pymysql.install_as_MySQLdb()

class Shop99114Pipeline(object):

    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            database='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.conn.ping(reconnect=True)
        self.cursor.execute('''INSERT INTO shop99114(com_name, cont_name, jingyingmoshi, zhuyingyewu, loc, 
        mobile, dianhua, chuanzhen, youxiang, address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
        (item['com_name'], item['cont_name'], item['jingyingmoshi'], item['zhuyingyewu'], item['loc'],
         item['mobile'], item['dianhua'], item['chuanzhen'], item['youxiang'], item['address']))
        self.conn.commit()
        return item



    def close(self, spider):

        pass