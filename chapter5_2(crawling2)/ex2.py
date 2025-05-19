# aiohttp 를 이용한 매우 빠른 크롤링(비동기적)
# Requests 모듈은 동기적으로 동작함.
# pip install aiohttp aiodns cchardet

# 상품 정보의 댓글들을 comments.json에 저장하는 프로그램
import requests
from bs4 import BeautifulSoup
from time import time
import asyncio
import aiohttp
import json

page_urls=["https://shop.hakhub.net/page/1/", "https://shop.hakhub.net/page/2/"]
json_path="./comments.json"

def get_product_urls(urls):
    # 모든 상품의 URL 반환

    product_urls = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        elem_li = soup.find_all("li", {"class": "product"})
        for li in elem_li:
            product_urls.append(li.find("a")["href"])
    print(f"{len(product_urls)}개의 상품이 존재합니다.")
    return product_urls

async def async_func(urls):
    # 같은 TCP 세션을 사용함. tcp 소켓을 생성
    # 내부적으로 http 헤더에 "keep-alive" 값을 설정해 하나의 tcp 세션을 끊지않고 작업
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as s:
        # 생성된 세션 객체를 show_product_review()에 넘김
        futures=[asyncio.create_task(show_product_review(s, url)) for url in urls]
        results = await asyncio.gather(*futures)
    
    with open(json_path, "w", encoding="utf-8") as f:
        print(f"JSON file save as: {json_path}")
        # dump 함수는 JSON 형태로 가공(직렬화)함. indent는 들여쓰기 설정
        json.dump(results, f, indent=4, ensure_ascii=False)


# aiohttp 모듈의 세션을 생성하고 비동기로 이용, product_name을 기준으로 각 댓글을 수집
async def show_product_review(s, url):
    async with s.get(url) as r:
        html = await r.text()
    soup = BeautifulSoup(html, "html.parser")
    product_name = soup.find("h1").text
    comments = soup.find_all("div", {"class": "comment-text"})
    comment_dict={}
    comment_dict["product_name"]=product_name
    comment_array=[]

    for comment in comments:
        comment_array.append(
            {
                "author":comment.find(
                    "strong", {"class": "woocommerce-review__author"}
                ).text,
                "rating": comment.find("strong", {"class": "rating"}).text,
                "datetime": comment.find("time")["datetime"],
                "description": comment.find("div", {"class": "description"}).text,

            }
        )
    comment_dict["comments"] = comment_array
    return comment_dict


if __name__ == '__main__':
    begin = time()
    product_urls = get_product_urls(page_urls)
    asyncio.run(async_func(product_urls))
    end = time()
    print(f"실행시간: {end-begin}")