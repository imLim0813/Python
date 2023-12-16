import requests
from bs4 import BeautifulSoup

PAGE = "http://v.media.daum.net/v/20170615203441266"

res = requests.get(PAGE)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find('title')
print(data.get_text())
print(soup.find('h3').get_text())