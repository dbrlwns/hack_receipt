# async 
# 제네레이터 예제
def generator():
    for i in range(3):
        yield i

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # StopInteration Error
        