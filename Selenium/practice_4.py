# 기존 크롤링 방식으로는 동적 웹페이지 정보를 가져오는게 불가능하다.
# ex) 네이버 뉴스 댓글

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=headless_options)
driver.get("https://n.news.naver.com/mnews/article/comment/016/0002243298?sid=105")

try:
    while True:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "u_cbox_page_more"))
        )
        driver.find_element(by=By.CLASS_NAME, value="u_cbox_page_more").click()
except Exception as e:
    pass


comments_list = driver.find_elements(by=By.CLASS_NAME, value="u_cbox_area")
for idx, comment in enumerate(comments_list):
    try:
        print(idx, comment.find_element(by=By.CLASS_NAME, value="u_cbox_contents").text)
    except:
        print(idx, "삭제된 댓글입니다..")

driver.quit()