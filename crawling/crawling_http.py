import requests
from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/xxx")

if res.status_code != 200:
    print("페이지 없음")
else:
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select("h4.card-text")

    for item in data:
        print(item.get_text())