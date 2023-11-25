import socket
import sys
import re
import logging
import os

host = "10.33.76.234"
port = 13337

os.makedirs("./logs", exist_ok=True)


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler("./logs/bs_client.log"), logging.StreamHandler(sys.stdout)],)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    logging.error(f"Impossible de se connecter au serveur {host} sur le port {port}")
    print(f"Impossible de se connecter au serveur {host} sur le port {port}")
    exit(1)
else:
    logging.info(f"Connexion réussie à {host}:{port}")
print("Bienvenue dans la calculatrice en réseau !")
print("Vous pouvez envoyer un calcul simple dans le format suivant \"1+1\".")
print("Vous pouvez utilitsez les symbols \"+, -, *\"")
print("Les chiffres ne peuvent excéder 10 000 (valeur négative et positive)\n")

while True:
    message = input("Que veux-tu envoyer au serveur : ")
    if type(message) != str:
        raise TypeError("Ici on veut que des strings !")
    elif not bool(message.match(r'^(-?\d{1,4})\s*([-+*])\s*(-?\d{1,4})$')):
        raise TypeError("Ton calcule n'est pas bon !")
    else:
        if message == "stop":
            s.close()
            sys.exit(0)
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