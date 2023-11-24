import socket
import sys
import re

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

while True:
    message = input("Que veux-tu envoyer au serveur : ")
    if type(message) != str:
        raise TypeError("Ici on veut que des strings !")
    elif not bool(re.fullmatch(r'meo|waf', message)):
        raise TypeError("On ne veut pas d'humain !")
    else:
        break

try:
    s.sendall(message.encode())
    data = s.recv(1024)
except Exception as e:
    print(e)
    s.close()
    sys.exit(1)

print(data.decode())
s.close()
sys.exit(0)