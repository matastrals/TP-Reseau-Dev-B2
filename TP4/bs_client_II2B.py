import socket
import sys
import re
import logging
import os

host = "10.33.76.234"
port = 13337

os.makedirs("./logs", exist_ok=True)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler("/var/log/bs_server/bs_server.log"), logging.StreamHandler(sys.stdout)],)
info_formatter = logging.Formatter('%(asctime)s - \033[91m%(levelname)s\033[0m - %(message)s')
info_handler = logging.StreamHandler()
info_handler.setLevel(logging.ERROR)
info_handler.setFormatter(info_formatter)
logging.getLogger().addHandler(info_handler)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    logging.error(f"Impossible de se connecter au serveur {host} sur le port {port}")
    print(f"Impossible de se connecter au serveur {host} sur le port {port}")
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