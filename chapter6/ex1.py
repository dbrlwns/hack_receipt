# https://whois.kr에서 도메인 정보를 조회하는 프로그램
# pip install python-whois, ISP(통신사)나 Cloud플랫폼 정보를 알수잇음
import whois
import socket

url = "hakhub.net"

try:
    url_info = whois.whois(url)
    ip = socket.gethostbyname(url) # DNS -> IP 반환
    print('='*50)
    print("<<URL Info>>")
    print(url_info)
    
    ip_info = whois.whois(ip)
    print('='*50)
    print("<<IP Info>>")
    print(ip_info)

except whois.parser.PywhoisError:
    print("Unregistered") # 미등록된 도메인 시 실행