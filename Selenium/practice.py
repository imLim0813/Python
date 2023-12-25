import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.python.org/"
driver.get(url)

assert "Python" in driver.title

elem = driver.find_element(by=By.NAME, value='q')
elem.send_keys('python')
elem.send_keys(Keys.RETURN)
time.sleep(2)

h3s = driver.find_elements(by=By.TAG_NAME, value='h3')
for h3 in h3s:
    print(h3.text )
driver.quit()