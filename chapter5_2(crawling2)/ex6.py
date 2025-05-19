# Selenium을 Beautifulsoup와 조합해서 사용
# 이 방법으로 SPA로 구현된 웹 페이지고 Parsing이 가능함.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep

url = "https://shop.hakhub.net"
user_id = "customer01"
user_pwd = "customer01!!"

def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")
    options.add_argument("lang=ko_KR")

    service = Service(executable_path="drivers/chromedriver")
    return webdriver.Chrome(service=service, options=options)


def get_item_info():
    driver.get(url)
    driver.implicitly_wait(3)
    html = driver.page_source # 웹 소스 불러오기
    soup = BeautifulSoup(html, "html.parser") # Parsing
    items = soup.find_all("li", {"class": "product"})
    for index, item in enumerate(items):
        print("===========")
        print(f"{index+1}번째 상품 ", end="")
        print(item.text)
    driver.close()


if __name__ == '__main__':
    driver = load_driver()
    get_item_info()
