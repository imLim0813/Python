import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawl_test")
soup = BeautifulSoup(res.content, 'html.parser')

# 한번 크게 감싸고, 세분화해서 감싸면 유용.
section = soup.find('ul', id='dev_course_list')
titles = section.find_all("li", "course")

for idx, title in enumerate(titles):
    print(f'{idx+1}.', title.get_text().split('[')[0].split('-')[1].strip())