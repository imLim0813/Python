import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawl_test_css.html")
soup = BeautifulSoup(res.content, 'html.parser')

# Select
items = soup.select("ul#hobby_course_list li.course")
for item in items:
    print(item.get_text())

# Select one
item = soup.select_one("ul#dev_course_list > li.course.paid")
print(item.get_text())

