import socket
import sys

host = "10.33.76.200" 
port = 13337              


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

try:
    s.sendall(b"Meooooo !")
    data = s.recv(1024)

except Exception as e:
    sys.exit(1)

finally:
    print(repr(data))
    s.close()
    sys.exit(0)