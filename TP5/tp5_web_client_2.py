import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

try:
    send = "GET /"
    s.send(send.encode())
    data = s.recv(1024)
    print(data.decode())
    
finally:
    s.close()