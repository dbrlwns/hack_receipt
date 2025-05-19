# Web Path Scanner
# 대상 웹 페이지의 디렉터리 목록과 방문할 페이지 링크를 수집해보자
# <a href로 시작하는 태그 가져오기로 시작
import requests
from bs4 import BeautifulSoup, SoupStrainer

target_domain = "https://shop.hakhub.net"
content = requests.get(target_domain).content

links = set() # 중복 제거되는 자료구조
# SoupStrainer은 Beautifulsoup에 추출할 부분을 알려주고 구문분석시 조건에 맞는 요소만 구성할 수 있다.
# 필요한 정보를 html의 특정 부분으로 좁혀 검색 결과를 빠르게 할 수 있다.
for link in BeautifulSoup(content, features="html.parser", parse_only=SoupStrainer("a")):
    if hasattr(link, "href"):
        path = link["href"]
        if target_domain not in path and path[:4] != "http":
            links.add(target_domain+path) # 상대경로를 절대경로로 가져옴
        else: 
            links.add(path)

for link in links:
    print(link)
