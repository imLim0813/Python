import requests
from bs4 import BeautifulSoup

PAGE = "http://v.media.daum.net/v/20170615203441266"

res = requests.get(PAGE)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find('title')
print(data.get_text())
print(soup.find('h3', "tit_view").get_text())
print(soup.find('h3', class_="tit_view").get_text())

data = soup.find_all('span', class_="txt_info")
for item in data:
    print(item.get_text())

print(soup.find('div', "layer_body").get_text())