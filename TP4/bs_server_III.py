import socket
import sys
import argparse
import logging
import datetime
import os
import select

os.makedirs("/var/log/calculator_server", exist_ok=True)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler("/var/log/bs_server/bs_server.log"), logging.StreamHandler(sys.stdout)],)

host="10.33.76.234"

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", help="open on a specific port")
args = parser.parse_args()

port = args.port

if (port == None):
    port = 13337

if (port < 0 or port > 65535):
    raise ValueError("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")

if (port > 0 and port < 1024):
    raise ValueError("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))  
s.listen(1)
logging.info(f'Le serveur tourne sur {host}:{port}')

# Configuration du timeout
s.settimeout(10)  # Timeout de 10 secondes

s.setblocking(False)

# Initialisation de lastTime
lastTime = datetime.datetime.now()

while True:
    # Utiliser select pour attendre la connexion avec un timeout
    readable, _, _ = select.select([s], [], [], 10)
    if s in readable:
        conn, addr = s.accept()
        print(f"Connexion établie avec {addr}")
        # Faire quelque chose avec la connexion, si nécessaire
        break
    period = datetime.datetime.now()
    if (period - lastTime).total_seconds() >= 60:
        logging.warning('Aucun client depuis plus de 60 secondes.')
        lastTime = period

logging.info(f'Un client {addr[0]} s\'est connecté.')
lastTime = datetime.datetime.now()

while True:
    # Reçoit les données du client
    data = conn.recv(1024)
    if data:
        logging.info(f'Le client {addr[0]} a envoyé {data.decode()}')
        message = eval(data.decode())
        message = str(message)
        conn.sendall(message.encode())
        logging.info(f'Réponse envoyée au client {addr[0]} : {message}')
        data = ""
    else:
        # Ferme le serveur si le client n'envoie pas de données pendant 60 seconds
        period = datetime.datetime.now()
        if (period - lastTime).total_seconds() >= 60:
            logging.warning('Aucune données reçu pendant plus de 60 secondes.')
            lastTime = period
            break

logging.info(f'Fermeture du serveur.')
conn.close()
sys.exit(0)

