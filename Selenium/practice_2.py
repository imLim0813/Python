import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "http://www.python.org"
driver.get(url)

assert "Python" in driver.title

search = driver.find_element(by=By.NAME, value='q')
search.clear()
search.send_keys("python")
search.send_keys(Keys.RETURN)

time.sleep(2)

assert "No results found." not in driver.page_source

data = driver.find_elements(by=By.CSS_SELECTOR, value="#content > div > section > form > ul > li > h3 > a")

for item in data:
    print(item.text)
driver.quit()

# Chrome 창을 띄우지 않고, 크롤링하기 위해 PhantomJS나 headless chrome을 사용하기도 한다.
# 더이상, PhantomJS 지원 안한다.