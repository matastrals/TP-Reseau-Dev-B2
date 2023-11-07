import socket
import sys

host="10.33.76.234"
port=13_337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))  
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
while True:

    try:
        data = conn.recv(1024)
        if not data: break

        print(data)

        conn.sendall(b"Hi mate !")

    except socket.error:
        print("Error Occured.")
        sys.exit(1)
        break


conn.close()
sys.exit(0)