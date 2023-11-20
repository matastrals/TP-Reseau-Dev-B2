import socket
import sys

host = "10.33.76.234"
port = 13337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    print(f"Error when trying to connect at {host} sur le port {port}")
    exit(1)
else:
    print(f"Connecté avec succès au serveur {host} sur le port {port}" )

message = input("Que veux-tu envoyer au serveur : ")
try:
    s.sendall(message.encode())
    data = s.recv(1024)
except Exception as e:
    print(e)
    s.close()
    sys.exit(1)

print(repr(data))
s.close()
sys.exit(0)