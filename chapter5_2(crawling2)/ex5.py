# XPath와 CSS Selector로 4개 상품을 장바구니로 넣어보자
# 2개는 XPath로, 2개는 CSS Selector로 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://shop.hakhub.net"
user_id = "customer01"
user_pwd = "customer01!!"

# 크롬드라이버 설정 및 반환
def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")
    options.add_argument("lang=ko_KR")

    service = Service(executable_path="drivers/chromedriver")
    return webdriver.Chrome(service=service, options=options)


def add_cart():
    driver.get(url)
    driver.implicitly_wait(3)

    driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[1]/a[2]').click()
    driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[2]/a[2]').click()
    driver.find_element(By.CSS_SELECTOR, 
                        '#main > ul > li.product.type-product.post-53.status-publish.instock.product_cat-clothing.product_cat-hoodies.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
    driver.find_element(By.CSS_SELECTOR, 
                        '#main > ul > li.product.type-product.post-31.status-publish.last.instock.product_cat-clothing.product_cat-t-shirts.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
    input("Enter 입력 시 종료")
                        

if __name__ == '__main__':
    driver = load_driver()
    add_cart()
