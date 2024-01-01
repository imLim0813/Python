import scrapy
from ecommerce.items import EcommerceItem

class GmarketBestSpider(scrapy.Spider):
    name = "gmarket_best"
    start_urls = ["http://www.gmarket.co.kr/n/best"]

    def parse(self, response):
        titles = response.css('div.best-list > ul > li > a::text').getall()
        prices = response.css('div.best-list > ul > li > div.item_price > div.s-price > strong > span::text').getall()
        
        for idx, title in enumerate(titles):
            item = EcommerceItem()
            item['title'] = title
            item['price'] = prices[idx]
            # item['price'] = (price.strip().replace("원", "").replace(",", ""))
            yield item

