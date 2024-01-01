import scrapy


class Test1Spider(scrapy.Spider):
    name = "test1"
    start_urls = ["http://www.gmarket.co.kr/n/best", "https://promotion.gmarket.co.kr/Event/CouponZone.asp"]

    def parse(self, response):
        print(response.url)
