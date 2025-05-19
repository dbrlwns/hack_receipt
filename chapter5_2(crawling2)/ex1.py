# BeautifulSoup를 이용한 상품 정보 크롤링
import requests
from bs4 import BeautifulSoup

url = "https://shop.hakhub.net/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
# print("=========Title=========")
# print(soup.title)
# print("=========Head=========")
# print(str(soup.head)[:300])
# print("=========Head>Link=========")
# print(soup.head.link)
# print("=========Body=========")
# print(str(soup.body)[:300])


elem_li = soup.find_all("li", {"class": "product"})

#for index, li in enumerate(elem_li):
    #print(f"\n========={index+1}번 상품=========")
    #print(li)

for index, li in enumerate(elem_li):
    print(f"\n==={index+1}번 상품===")
    print(li.find("h2", {"class": "woocommerce-loop-product__title"}).text)
    print(li.find("span", {"class": "price"}).text)
    try:
        print(li.find("strong", {"class": "rating"}).text)
    except Exception as e:
        print("가격 정보 없음")
