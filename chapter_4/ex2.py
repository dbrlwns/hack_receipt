# Raw socket을 이용한 IP Header analysis
from socket import *
import os, struct

def parsing(host):
    # raw socket 생성과 bind
    sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
    sock.bind((host, 0))

    # socket option
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    packet_num=0
    try:
        while True:
            packet_num += 1
            data = sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_ip_header(data[0])
            print(f"{packet_num} th packet\n")
            print("version: ", ip_headers[0]>>4) # 1Byte로 왼쪽 1nib은 ip버전
            print("Header Length: ", ip_headers[0] & 0x0F) # 단위는 워드
            print("Type of Service: ", ip_headers[1])
            print("Total Length: ", ip_headers[2])
            print("Identification: ", ip_headers[3])
            print("IP Flags, Fragment Offset: ", flags_and_offset(ip_headers[4]))
            print("Time To Live: ", ip_headers[5])
            print("Protocol: ", ip_headers[6])
            print("Header Checksum: ", ip_headers[7])
            # inet_ntoa()는 byte형을 우리가 읽을 수 있는 IP주소 체계로 보여줌.
            print("Source Address: ", inet_ntoa(ip_headers[8]))
            print("Destination Address: ", inet_ntoa(ip_headers[9]))
            print("="*50)
    except KeyboardInterrupt: # Ctrl-C
        sock.close()


# struct 모듈로 byte를 다루기 편함.
def parse_ip_header(ip_header): # 패킷을 Byte 형태로 넣음
    # B:1byte, H:2byte, s:1byte
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads # 헤더와 나머지로 반환


# 숫자를 byte 형태로 변환 후 bit 형태로 출력
def flags_and_offset(int_num):
    byte_num = int_num.to_bytes(2, byteorder="big") # 2bytes 길이의 big-endian
    x = bytearray(byte_num)
    # 1byte = 8bits이므로 zfill()로 자릿수 맞춤
    flags_and_flagment_offset = bin(x[0])[2:].zfill(8) + \
                                    bin(x[1])[2:].zfill(8)
    return(flags_and_flagment_offset[:3],
           flags_and_flagment_offset[3:])

if __name__ == '__main__':
    host = "192.168.0.246"
    print(f"Listening at ({host})")
    parsing(host)
        