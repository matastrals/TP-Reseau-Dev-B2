import socket
import sys
import argparse
import logging
import datetime
import os

os.makedirs("/var/log/bs_server", exist_ok=True)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.FileHandler("/var/log/bs_server/bs_server.log"), logging.StreamHandler(sys.stdout)],)

host=""

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

try:
    lastTime = datetime.datetime.now()
    period = datetime.datetime.now()
    if (lastTime - period).total_seconds() == 30:
        logging.warn(f'Aucun client depuis plus de une minute.')
        lastTime = period
    conn, addr = s.accept()
except:
    print("Error")
    sys.exit(1)
else:
    logging.info(f'Un client {addr[0]} s\'est connecté.')

while True:
    # Reçoit les données du client
    data = conn.recv(1024)
    
    if data.decode().__contains__("meo"):
        message = "Meo a toi confrere."
        conn.sendall(message.encode())
        logging.info(f'Réponse envoyée au client {addr[0]} : {message}')
        break
    elif data.decode().__contains__("waf"):
        message = "ptdr t ki"
        conn.sendall(message.encode())
        logging.info(f'Réponse envoyée au client {addr[0]} : {message}')
        break

            
conn.close()
sys.exit(0)
