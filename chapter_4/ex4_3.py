# ping sweep scanner
# ICMP Echo Request를 이용하여
# IP 범위를 쓸고 지나가면서 존재하는 호스트 찾아내기

from pythonping import ping
from time import time

def icmp_scan():
    ip_addresses = ["33.22.143.1", "8.8.8.8", "google.com"]
    for ip_address in ip_addresses:
        print(f"Ping Target => {ip_address}")
        ping(ip_address, timeout=1, count=1, verbose=True)



if __name__ == '__main__':
    begin = time()
    icmp_scan()
    end = time()
    print(f"실행 시간 : {end - begin}")
    # 여긴 동기적으로 실행해서 1000번하면 오래걸림
    