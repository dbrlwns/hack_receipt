# FastApi, uvicorn(웹 서버와 웹 앱의 인터페이스 역할)
import uvicorn
from typing import Optional
from fastapi import FastAPI

app = FastAPI()
animals = {"cat": "meow", "dog": "bark", "duck":"quack"}

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.get("/animals/{animal}")
async def animal_cry(animal: str, cry:Optional[int]):
    # cry 횟수만큼 출력
    sound=""
    for time in range(cry):
        sound = sound+animals[animal]+" "
    return {"animal": animal, "sound": sound.strip()}


if __name__ == '__main__':
    # 첫 번째 인자를 파일명으로 해야함. app은 위에 선언된 fastapi 인스턴스
    uvicorn.run("ex1:app", host="0.0.0.0", port=80, reload=True)

# localhost/docs에 접속하면 Swagger 기반의 문서가 출력됨. 요청을 할 수 있음.