import re, requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawling_stock_example.html")
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select("li.row_sty")

for item in data:
    name = item.find("div", class_="st_name")
    price = item.find("div", class_="st_price")
    rate = item.find("div", class_="st_rate")

    name = re.sub("[\n\t\s]", "", name.get_text())
    price = re.sub("[\n\t\s]", "", price.get_text())
    rate = re.sub("[\n\t\s]", "", rate.get_text())
    print(f'{name} {price} {rate}')