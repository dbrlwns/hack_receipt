# Directory Scanner 구현
# 사이트가 포함하는 하위 디렉토리를 탐색
# 사전 파일을 대입하여 디렉터리 구조를 파악하는데 숨겨진 디렉터리도 포함됨

from time import time
import asyncio
import aiohttp
import aiohttp.client_exceptions

# Wordprocess Dictionary File
directory_list_path = "./wp-directory.txt"
target_domain = "https://shop.hakhub.net"

async def async_func(directory_list):
    conn = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as s:
        futures = [
            asyncio.create_task(find_directory(s, f"{target_domain}/{directory}"))
            for directory in directory_list
        ]
        results = await asyncio.gather(*futures)
        #for result in results:
         #   if result is not None:
          #      write_result(result)

async def find_directory(s, sub_directory_path):
    try:
        async with s.get(sub_directory_path) as r:
            if r.status == 200:
                output = (sub_directory_path, r.status)
                print(output)
                return output
            elif r.status == 404:
                pass
            else:
                raise Exception("status_code", r.status)
    
    except aiohttp.client_exceptions.ClientConnectionError as e:
        # Get Address info failed Error...
        pass
    except Exception as e:
        status_code, error_status = e.args
        output = (sub_directory_path, error_status)
        print(output)
        return output
    

if __name__ == '__main__':
    begin = time() 
    directory_list = open(directory_list_path).read().splitlines()
    asyncio.run(async_func(directory_list))
    end = time()
    print(f"실행 시간: {end-begin}")



"""

이러한 스캔동작은 대상 웹 서버에 많은 쿼리를 생성하고 느려지게 할 수 있다.
실제 웹 서비스가 이루어지는 곳에 수행하면 안된다.

"""