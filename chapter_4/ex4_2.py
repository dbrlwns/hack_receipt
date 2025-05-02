# File transfer ( Server )
from pythonping import ping
from time import sleep

with open("./send_logo.png", "rb") as f:
    while True:
        byte = f.read(1024)
        if byte==b"": # EOF, Null
            ping("172.16.12.70", verbose=True, count=1, payload=b"EOF")
            break
        ping("172.16.12.70", verbose=True, count=1, payload=byte)
        sleep(0.5)

# 패킷은 원래 송수신의 순서를 보장 안함