from pythonping import ping
 
# sudo python ex1.py 로 해야하넹..

# ping("8.8.8.8", verbose=True, count=1)
# ping("100.100.100.255", verbose=True, count=1)



# 사용할때마다 conda activate py3.9로 가상환경을 활성화시켜야함.

from utils.display import delay_print
print(f"__name__ : {__name__}")
delay_print("한 글자씨 ㄱ끊어 출력하기")
