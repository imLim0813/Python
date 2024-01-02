import scrapy
from ecommerce.items import EcommerceItem

class GmarketCategoryAllSpider(scrapy.Spider):
    name = "gmarket_category_all"

    def start_requests(self):
        yield scrapy.Request(url="http://www.gmarket.co.kr/n/best", callback=self.parse_mainpages)

    def parse_mainpages(self, response):
        print("parse_mainpages")
        category_links = response.css("div.gbest-cate ul li a::attr(href)").getall()
        category_names = response.css("div.gbest-cate ul li a::text").getall()

        # 1st category
        for name, link in zip(category_names, category_links):
            yield scrapy.Request(url="http://www.gmarket.co.kr" + link, callback=self.parse_items, meta={"main_category_name" : name, "sub_category_name" : 'ALL'})

        # 2nd category
        for name, link in zip(category_names, category_links):
            yield scrapy.Request(url="http://www.gmarket.co.kr" + link, callback=self.parse_sub_category, meta={"main_category_name" : name})

    def parse_sub_category(self, response):
        print("parse_sub_category", response.meta['main_category_name'])
        sub_category_links = response.css('div.navi.group > ul > li > a::attr(href)').getall()
        sub_category_names = response.css('div.navi.group > ul > li > a::text').getall()

        for name, link in zip(sub_category_names, sub_category_links):
            # print("http://www.gmarket.co.kr" + link, name) 
            yield scrapy.Request(url="http://www.gmarket.co.kr" + link, callback=self.parse_items, meta={"main_category_name" : response.meta['main_category_name'], "sub_category_name" : name})


    def parse_items(self, response):
        print("parse_main_category", response.meta['main_category_name'])
        
        best_items = response.css("div.best-list")

        for idx, item in enumerate(best_items.css("li")):
            doc = EcommerceItem()
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


            doc['main_category_name'] = response.meta['main_category_name']
            doc['sub_category_name'] = response.meta['sub_category_name']
            doc['ranking'] = idx+1
            doc['title'] = title
            doc['orig_price'] = orig_price
            doc['discount_price'] = discount_price
            doc['discount_percent'] = discount_percent
            
            # print(idx + 1, title, orig_price, discount_price, discount_percent)
            yield doc
