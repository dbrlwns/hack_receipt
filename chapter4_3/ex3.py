# ICMP 스캐너 (비동기 이용)
from time import time
import asyncio
from pythonping import ping
import ipaddress
from functools import partial

target_network = "192.168.0.0/24"
# ipaddress : CIDR 표기법을 이용, 
# IP주소 범위를 나타내는 형식을 이용해 배열 생성
net4 = ipaddress.ip_network(target_network)
ip_addresses=[]
for ip in net4.hosts():
    ip_addresses.append(str(ip))

async def async_func():
    print(f"Target Network: {target_network}")
    # 저수준 함수 ensure_future
    futures = [asyncio.ensure_future(do_ping(ip)) for ip in ip_addresses]
    results = await asyncio.gather(*futures)
    for result in results:
        if result["Echo Reply"]:
            print(result)

async def async_func2():
    print(f"Target Network: {target_network}")
    loop = asyncio.get_running_loop()

    # 고수준 함수 create_task,
    # coroutine을 Task로 감싼 클래스 객체 반환
    cos = [asyncio.create_task(do_ping(ip)) for ip in ip_addresses]
    results = await asyncio.gather(*cos)
    for result in results:
        if result["Echo Reply"]:
            print(result)

async def do_ping(ip):
    # 동기로 작성된 ping 함수를 비동기 코루틴으로 감쌈
    # 키워드 인자 전달을 위해 partial 사용
    loop = asyncio.get_event_loop()
    ping_request = partial(ping, ip, timeout=1, count=1)
    resp = await loop.run_in_executor(None, ping_request)
    return {
        "IP": ip,
        "Echo Reply": resp._responses[0].success,
        "Verbose": resp._responses[0],
    }

if __name__ == '__main__':
    begin = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_func2())
    loop.close()
    end = time()
    print(f"실행 시간 : {end - begin}")