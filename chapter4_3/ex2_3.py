import asyncio

async def main():
    await asyncio.sleep(0)
    return 42

# 
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# try:
#     print(loop.run_until_complete(main()))
# finally:
#     asyncio.set_event_loop(None)
#     loop.close()

# 위의 코드와 같지만 
# 고수준 함수인 asyncio.run() 을 사용함.
print(asyncio.run(main())) 