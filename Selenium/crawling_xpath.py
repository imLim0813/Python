# 1.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

headless_options = webdriver.ChromeOptions()
headless_options.add_argument("headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=headless_options)
driver.get("https://v.daum.net/v/20170922175202762")

title = driver.find_element(by=By.XPATH, value="//title")
print(title.get_attribute("text"))
driver.quit()
