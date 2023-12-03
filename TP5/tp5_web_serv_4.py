import socket
import sys
import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.StreamHandler(sys.stdout)],)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8080))  


s.listen(1)
conn, addr = s.accept()

while True:
    request = conn.recv(4)
    request = request.decode()
    if request[0:4] == "GET ":
        get_request = conn.recv(50)
        resultat = re.search(r'([^ ]*) ', get_request.decode())
        print(resultat.group(1))

        file = open("." + resultat.group(1))
        html_content = file.read()
        file.close()

        http_response = 'HTTP/1.0 200 OK\n\n' + html_content
        conn.send(http_response.encode())
        logging.info(f"{request}{resultat.group(1)}")

sys.exit(0)
