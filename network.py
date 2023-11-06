import psutil
import socket
import os
from sys import argv

def Lookup(arg):
    response = socket.gethostbyname(arg)
    return response

def Is_Up(arg):
    if os.system(f"ping {arg} > ./null ") == 0:
        return "UP !"
    else:
       return "DOWN !"

def Get_Ip():
    for interface, addrs in psutil.net_if_addrs().items():
        if "Wi-Fi" in interface:  
            for addr in addrs:
                if addr.family == socket.AF_INET:  
                    return addr.address
    return None

response = ""
match (argv[1]):
    case "lookup":
        response = Lookup(argv[2])
    case "ping":
        response = Is_Up(argv[2])
    case "ip":
        response = Get_Ip()
    case _:
        response = "is not an available command. Be better."
print(f"{argv[1]} {response}")

