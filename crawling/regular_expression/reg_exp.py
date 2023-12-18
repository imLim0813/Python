import requests, re
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawl_test_css.html")
soup = BeautifulSoup(res.content, 'html.parser')

# Select
items = soup.select("ul#dev_course_list li.course")
for item in items:
    print(re.sub("\[[0-9]+\]", "", item.get_text()))
