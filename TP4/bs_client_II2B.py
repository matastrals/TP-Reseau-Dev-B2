import socket
import sys
import re
import logging

host = "192.168.1.98"
port = 13337

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler("/var/log/bs_server/bs_server.log"), logging.StreamHandler(sys.stdout)],)
logging.basicConfig(level=logging.ERROR, format='\033[0m%(asctime)s - \033[91m%(levelname)s\033[0m - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler("/var/log/bs_server/bs_server.log"), logging.StreamHandler(sys.stdout)],)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    logging.info(f"Connexion réussie à {host}:{port}")
    exit(1)
else:
    logging.info(f"Connexion réussie à {host}:{port}")

while True:
    message = input("Que veux-tu envoyer au serveur : ")
    if type(message) != str:
        raise TypeError("Ici on veut que des strings !")
    elif not bool(re.fullmatch(r'meo|waf', message)):
        raise TypeError("On ne veut pas d'humain !")
    else:
        break

try:
    logging.info(f"Message envoyée au serveur {host} : {message}")
    s.sendall(message.encode())
    data = s.recv(1024)
    logging.info(f"Réponse reçue du serveur {host} : {data.decode()}")
except Exception as e:
    print(e)
    s.close()
    sys.exit(1)

print(data.decode())
s.close()
sys.exit(0)