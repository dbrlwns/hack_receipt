# chromedriver 설치 후 상품 정보를 스크린샷으로 저장하는 예제
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service

url = "https://shop.hakhub.net/product/flying-ninja/"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")
options.add_argument("lang=ko_KR")

service = Service(executable_path="drivers/chromedriver")
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
driver.implicitly_wait(3)
driver.get_screenshot_as_file("web.png")

Image.open("web.png").convert("RGB").save("web.jpg", quality=100)
im = Image.open("web.jpg")
cropped_image = im.crop((280, 300, 1100, 780))
cropped_image.save("web_cropped.jpg", quality=100)

driver.close()