import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=headless_options)

url = "https://v.daum.net/v/20170202185812986"
driver.get(url)

title = driver.find_element(by=By.TAG_NAME, value='h3')
print(title.text)

title = driver.find_element(by=By.CLASS_NAME, value='tit_view')
print(title.text)

# title = driver.find_element(by=By.CSS_SELECTOR, value='#mArticle > div.news_view.fs_type1 > div.article_view > section > div:nth-child(4) > div > div')
# print(title.text)

title = driver.find_element(by=By.CSS_SELECTOR, value="div[dmcf-pid='nYgEcm4K5S']")
print(title.text)

titles = driver.find_elements(by=By.TAG_NAME, value='h3')

for title in titles:
    print(title.text)

driver.quit()