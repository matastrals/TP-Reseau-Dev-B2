import socket
import sys

host = "192.168.1.98"
port = 13337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    print(f"Error when trying to connect at {host} sur le port {port}")
    exit(1)
else:
    print(f"Connecté avec succès au serveur {host} sur le port {port}" )

try:
    s.sendall(b"Meooooo")
    data = s.recv(1024)

except Exception as e:
    sys.exit(1)

finally:
    print(data.decode())
    s.close()
    sys.exit(0)