import requests
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
params = {'serviceKey': '',
         'returnType': 'json',
         'numOfRows': '100',
         'pageNo': '1',
         'searchDate': '2020-11-14',
         'InformCode': 'PM10'}

res = requests.get(url, params)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)