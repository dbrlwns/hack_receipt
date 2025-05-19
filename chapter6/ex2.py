# subdomain scanner
# ex) example.com이 있으면 blog.example.com 처럼 서브도메인이 있다
from time import time
import asyncio
import aiohttp
import aiohttp.client_exceptions 

# Subdomain Dictionary File
# 여기서 사전 파일이란 공격에 대입할 단어들을 의미함
wordlist_path="./subdomains.txt"
target_domain= "google.com"

async def async_func(domains):
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as s:
        futures = [asyncio.create_task(discover_url(s, f"http://{domain}.{target_domain}")) for domain in domains]
        results = await asyncio.gather(*futures)
    #for result in results:
     #   if result is not None:
      #      print(result)


async def discover_url(s, domain):
    try:
        async with s.get(domain) as r:
            if r.status == 200:
                output = (domain, r.status)
                print(output)
                return output

            else:
                raise Exception("status_code", r.status)
    except aiohttp.client_exceptions.ClientConnectionError as e:
        # Get Address info failed Error...
        pass
    except Exception as e:
        status_code, error_status = e.args
        output = (domain, error_status)
        print(output)
        return output


if __name__ == '__main__':
    begin = time()
    subdomain_words = open(wordlist_path).read().splitlines()
    asyncio.run(async_func(subdomain_words))
    end = time()
    print(f"실행 시간: {end-begin}")

"""
만약 공격 대상에서 test.ex.com이나 dev.ex.com 등의 도메인 존재 시
실제 사이트보다 보안 수준이 낮을 가능성이 있다.

공격자는 떄로는 정공법보다 우회하는 방식을 선택하기도 한다.
"""