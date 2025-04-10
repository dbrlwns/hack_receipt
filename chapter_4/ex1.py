# simple socket telecommunication
from socket import *
import os

def parsing(host):
    # raw socket 생성 및 bind
    # SOCK_STREAM:TCP, SOCK_DGRAM:UDP, SOCK_RAW:raw socket
    sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
    sock.bind((host, 0)) 

    # 원래 Promiscuous 모드라고 해당 랜카드를 지나는 모든 요청을
    # 받는 모드가있는데 맥에서는 raw socket이 기본적으로 이 모드를 허용x

    # socket option(해당 프로토콜 대상으로 IP 헤더를 포함하는 옵션을 1로 설정)
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # 소켓에서 데이터를 수신할 버커 크기를 정의
    data = sock.recvfrom(65535)
    print(data[0])

    # 소켓 종료
    sock.close()

if __name__ == '__main__':
    host = "192.168.0.246"
    print(f"Listening at [{host}]")
    parsing(host)
    # ping host하면 패킷수신을 확인할 수 있음.