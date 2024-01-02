import scrapy, json

from naveropenapi.items import NaveropenapiItem

class NavershoppingSpider(scrapy.Spider):
    name = "navershopping"
    start_url = "https://openapi.naver.com/v1/search/shop.json?query="

    def start_requests(self):
        client_id = ''
        client_password = ''
        header_params = {'X-Naver-Client-Id' : client_id, 'X-Naver-Client-Secret' : client_password}
        query = 'iphone'
        yield scrapy.Request(url=self.start_url + query, headers = header_params)

    def parse(self, response):
        doc = NaveropenapiItem()
        data = json.loads(response.text)
        for item in data['items']:
            doc['title'] = item['title']
            doc['link'] = item['link']
            doc['image'] = item['image']
            doc['lprice'] = item['lprice']
            doc['hprice'] = item['hprice']
            doc['mallName'] = item['mallName']
            doc['productId'] = item['productId']
            doc['productType'] = item['productType']
            yield doc

