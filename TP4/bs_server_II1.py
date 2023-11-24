import socket
import sys
import argparse

host=""

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store", help="open on a specific port")
args = parser.parse_args()

port = int(args.port)

if (port == None):
    port = 13337

if (port < 0 or port > 65535):
    raise ValueError("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")

if (port > 0 and port < 1024):
    raise ValueError("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))  
s.listen(1)
try:
    conn, addr = s.accept()
except:
    print("Error")
    sys.exit(1)
else:
    print(f"Un client vient de se co et son IP c'est {addr[0]}")

while True:
    # Reçoit les données du client
    data = conn.recv(1024)
    if data.decode().__contains__("meo"):
        message = "Meo a toi confrere."
        conn.sendall(message.encode())
        break
    elif data.decode().__contains__("waf"):
        message = "ptdr t ki"
        conn.sendall(message.encode())
        break

            
conn.close()
sys.exit(0)
