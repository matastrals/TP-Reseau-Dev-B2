import socket
import sys
import re

host=""
port=13337

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
    else:
        message = "Mes respects humble humain."
        conn.sendall(message.encode())
        break
    
            
conn.close()
sys.exit(0)
