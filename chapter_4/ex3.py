# ICMP sniffer

from socket import *
import os, struct


def parse_in_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads

def parsse_icmp_header(icmp_data):
    icmp_headers = struct.unpack("!BBHHH", icmp_data[:8])
    icmp_payloads = icmp_data[8:]
    return icmp_headers, icmp_payloads


def parsing(host):
    # raw socket 생성과 bind
    sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
    sock.bind((host, 0))

    # socket option
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    try:
        while True:
            data = sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_in_header(data[0])
            if ip_headers[6] == 1: # only ICMP
                ip_source_address = inet_ntoa(ip_headers[8])
                ip_destination_address = inet_ntoa(ip_headers[9])
                print(f"{ip_source_address} => {ip_destination_address}")
                icmp_headers, icmp_payloads = parsse_icmp_header(ip_payloads)
                if icmp_headers[0] == 0:
                    print("Echo Reply")
                elif icmp_headers[0] == 8:
                    print("Echo Request")
                print("icmp_headers => ", icmp_headers)
                print("icmp_payloads => ", icmp_payloads)
                print("========================")
    
    except KeyboardInterrupt:
        sock.close()


if __name__ == '__main__':
    host = '192.168.0.246'
    print("Start Sniffing at [%s]" % host)
    parsing(host)