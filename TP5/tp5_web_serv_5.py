import socket
import sys
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.StreamHandler(sys.stdout)],)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8080))  


s.listen(1)
conn, addr = s.accept()

while True:
    request = ""
    request = conn.recv(1024)
    request = request.decode()
    if request[0:5] == "GET /":
        get_request = request[5:]
        resultat = re.search(r'([^ ]*) ', get_request)
        if resultat != None:
            if resultat.group(1) != " " and resultat.group(1) != "":
                file = open("./" + resultat.group(1), 'rb')
                html_content = file.read()
                file.close()

                if type(html_content) == "str":
                    http_response = 'HTTP/1.0 200 OK\n\n' + html_content
                    conn.send(http_response.encode())
                else:
                    http_response = 'HTTP/1.0 200 OK\n\n'
                    all_response = http_response.encode() + html_content
                    conn.send(all_response)                   
                logging.info(f"{resultat.group()}")
                break
            else:
                response = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>"
                conn.send(response.encode())
                break
        else:
            response = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>"
            conn.send(response.encode())
            break

sys.exit(0)


