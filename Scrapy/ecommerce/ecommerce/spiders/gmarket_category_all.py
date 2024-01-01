import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = "gmarket_category_all"

    def start_requests(self):
        yield scrapy.Request(url="http://www.gmarket.co.kr/n/best", callback=self.parse_mainpages)

    def parse_mainpages(self, response):
        print("parse_mainpages")
        category_links = response.css("div.gbest-cate ul li a::attr(href)").getall()
        category_names = response.css("div.gbest-cate ul li a::text").getall()

        for name, link in zip(category_names, category_links):
            yield scrapy.Request(url="http://www.gmarket.co.kr" + link, callback=self.parse_maincategory, meta={"maincategory_name" : name})

    def parse_maincategory(self, response):
        print("parse_maincategory", response.meta['maincategory_name'])
        
        best_items = response.css("div.best-list")

        for idx, item in enumerate(best_items.css("li")):
            title = item.css("a.itemname::text").get()

            discount_price = item.css("div.s-price strong span::text").getall()[0]
            try:
                orig_price = item.css("div.o-price span::text").getall()[1]
                discount_percent = item.css("div.s-price em::text").getall()[0]
            except:
                orig_price = discount_price
                discount_percent = '0'

            discount_price = int(discount_price.replace(",", ""))
            orig_price = int(orig_price.replace(",", ""))
            discount_percent = int(discount_percent)

            print(idx + 1, title, orig_price, discount_price, discount_percent)