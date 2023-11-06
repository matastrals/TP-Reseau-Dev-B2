import socket
from sys import argv

def GetHost(arg):
    response = socket.gethostbyname(arg)
    return response

print(GetHost(argv[1]))