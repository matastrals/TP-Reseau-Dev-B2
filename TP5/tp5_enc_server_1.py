import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        headerx = conn.recv(1)
        if not headerx: break
        headerx = int.from_bytes(headerx, byteorder='big')
        datax = conn.recv(headerx)
        if not datax: break
        datax = int.from_bytes(datax, byteorder='big')
        opérateur = conn.recv(1)
        if opérateur == b'\x01':
            opérateur = '+'
        elif opérateur == b'\x02':
            opérateur = '-'
        elif opérateur == b'\x03':
            opérateur = '*'

        headery = conn.recv(1)
        if not headery: break
        headery = int.from_bytes(headery, byteorder='big')
        datay = conn.recv(headery)
        if not datay: break
        datay = int.from_bytes(datay, byteorder='big')

        clapfin = conn.recv(1)
        if not clapfin:print("Toutes les données ne sont pas recu")
        clapfin = int.from_bytes(clapfin, byteorder='big')
        if clapfin != 0:print("Ya un probl ?")

        total_data = str(datax) + opérateur + str(datay)
        # Evaluation et envoi du résultat
        res  = eval(total_data)
        res = int(res)
        res = res.to_bytes(6, byteorder='big')
        conn.send(res)
        break
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
sys.exit(0)
