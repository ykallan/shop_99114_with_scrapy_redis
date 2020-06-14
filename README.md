# shop_99114_with_scrapy_redis
使用分布式爬取网站



设置步骤：

settings里：


SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

SCHEDULER_PERSIST = True  # 是否在关闭时候保留原来的调度器和去重记录，True=保留，False=清空

SCHEDULER_QUEUECLASS = 'scrapy_redis.queue.SpiderQueue'

REDIS_URL = 'redis://localhost:6379'  # redis服务器的地址


spider里：


from scrapy_redis.spiders import RedisSpider  # 引入RedisSpider

class HySpider(RedisSpider): # 让爬虫类继承 RedisSpider

start_urls = ['http://shop.99114.com/']  注释掉start_urls
redis_key = 'start_url'   添加一个key


其他地方不用修改



（1）在scrapy-master机器中 进入redis-cli 管理面板

lpush start_url http://shop.99114.com/    # lpush redis_key 需要爬取的网址入口（start_urls里面的内容）

（2）正常启动spider：
scrapy crawl spider_name

(1) (2) 没有先后顺序，如果是在局域网内，需要设置redis的配置文件  redis.windows.conf ：
把其中的：bind 127.0.0.1 注释掉



对于 scrapy_redis 的理解：

主机并不一定要安装scrapy，只是建立了redis数据库，当作调度，以及传入初始的start_url操作，并不会因为叫做scrapy_master，就运行爬虫的代码。在scrapy_slave中，爬虫类继承于引入的RedisSpider， 并设置一个redis_key，在master中lpush 一个redis_key start_url即可，两个redis_key名称要一致。
