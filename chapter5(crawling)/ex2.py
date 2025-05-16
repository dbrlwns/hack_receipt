# Request 모듈의 기초 사용법
import requests

url = "https://shop.hakhub.net"
r = requests.get(url)
print(f"Statud Code : {r.status_code}")
print(f"Response Header : {r.headers}")
print("Response Body")
print(r.text[:1000]) # 응답 객체의 HTML 내용이 담김


# HTTP는 무상태 프로토콜로 각각의 요청이 독립적임.