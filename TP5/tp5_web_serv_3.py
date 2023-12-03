import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8080))  

s.listen(1)
conn, addr = s.accept()

while True:
    request = conn.recv(1024)
    request = request.decode()
    if request[0:5] == "GET /" and request[6] == " ":
        print(request)
        response = "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>"
        conn.send(response.encode())
    elif request[len("GET /index.html")]:
        file = open('./index.html')
        html_content = file.read()
        file.close()

        http_response = 'HTTP/1.0 200 OK\n\n' + html_content
        conn.send(http_response.encode())

sys.exit(0)
