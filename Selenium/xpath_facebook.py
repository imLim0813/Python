
# 2. 페이스북
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.facebook.com/"
driver.get(url)

user_name = ""
password = ""

email_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='email']")))
password_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='pass']")))
login_button_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@name='login']")))

email_tag.clear()
email_tag.send_keys(user_name)

password_tag.clear()
password_tag.send_keys(password)

login_button_tag.click()

time.sleep(10)
driver.quit()