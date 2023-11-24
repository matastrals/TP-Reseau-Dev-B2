import socket
import sys
import re

host="10.33.76.234"
port=13_337

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
    data = conn.recv(1024)
    if type(data.decode()) != str:
        conn.close()
        raise TypeError("Ici on veut que des strings !")
    if bool(re.search(r'meo|waf', data.decode())) == False:
        conn.close()
        raise TypeError("On ne veut pas d'humain !")
    if data.decode().__contains__("meo"):
        message = "Meo a toi confrere."
        conn.sendall(message.encode())
        break
    elif data.decode().__contains__("waf"):
        message = "ptdr t ki"
        conn.sendall(message.encode())
        break
    else:
        print(data.decode(), bool(re.search(r'meo|waf', data.decode())))
        break
    
            
conn.close()
sys.exit(0)
