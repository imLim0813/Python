import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('tr')

for item in items:
    columns = item.select("td")
    row_str = ""
    for column in columns:
         row_str += ", " + column.get_text()
    print(row_str[2:])