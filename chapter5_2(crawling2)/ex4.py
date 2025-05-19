# selenium으로 웹 내 자동화
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://shop.hakhub.net/wp-login.php"
url2 = "https://shop.hakhub.net"
user_id = "customer01"
user_pwd = "customer01!!"

# 크롬드라이버 설정 및 반환
def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")
    options.add_argument("lang=ko_KR")

    service = Service(executable_path="drivers/chromedriver")
    return webdriver.Chrome(service=service, options=options)



# 로그인 시도, 화면 열리고 휘리릭 됨
def try_login():
    driver.get(url)
    driver.implicitly_wait(3)
    
    driver.find_element("name", "log").send_keys(user_id)
    
    driver.find_element("name", "pwd").send_keys(user_pwd)
    
    driver.find_element("name", "wp-submit").click()


# 홈페이지에서 상품정보만 가져와 출력하기
def get_product_title():
    driver.get(url2)
    driver.implicitly_wait(3)
    elements=driver.find_elements(By.CLASS_NAME, "woocommerce-loop-product__title")
    for element in elements:
        print(element.text)




if __name__ == '__main__':
    driver = load_driver()
    get_product_title()





"""

XPath : XML문서의 특정 부분을 가리킬 때 사용
/ : 최상위의 기준 루트노드
// : 지정된 노드에서부터 순차 탐색
. : 현재 노드를 선택
.. : 현재 노드의 부모 노드를 선택
@ : 속성 노드를 선택

"""