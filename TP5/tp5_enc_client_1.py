import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

while True:
    msg = input("Calcul à envoyer: ")
    msg = msg.split(" ")
    if len(msg) != 3:
        print("Le calcul doit être sous forme : \"x opérateur y\"")
        continue

    int_x = int(msg[0])

    try:
        bytes_x = int_x.to_bytes(4, byteorder='big')
    except:
        print("Les chiffres ne peuvent dépasser \"4294967295\"")
        continue

    lengthx = len(bytes_x)
    headerx = lengthx.to_bytes(1, byteorder='big')

    opérateur = msg[1]
    if opérateur == '+':
        opérateur = 1
    elif opérateur == '-':
        opérateur = 2
    elif opérateur == '*':
        opérateur = 3
    else:
        print("Les opérateurs sont \"+, -, *\"")
        continue

    opérateur = opérateur.to_bytes(1, byteorder='big')

    int_y = int(msg[2])

    try:
        bytes_y = int_y.to_bytes(4, byteorder='big')
    except:
        print("Les chiffres ne peuvent dépasser \"4294967295\"")
        continue

    lengthy = len(bytes_y)
    headery = lengthy.to_bytes(1, byteorder='big')
    break

clapfin = 0
clapfin = clapfin.to_bytes(1, byteorder='big')
payload = headerx + bytes_x + opérateur + headery + bytes_y + clapfin
s.send(payload)

s_data = s.recv(6)
s_data = int.from_bytes(s_data, byteorder='big')
print(s_data)

s.close()
sys.exit(0)
