import psutil
import socket
import os
from sys import argv

def Lookup(arg):
    response = socket.gethostbyname(arg)
    return response

def Is_Up(arg):
    if os.system(f"ping -c 2 {arg} > ./null ") == 0:
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
if len(argv) >= 3:
    command = argv[1]
    if command == "lookup":
        response = Lookup(argv[2])
    elif command == "ping":
        response = Is_Up(argv[2])
    elif command == "ip":
        response = Get_Ip()
    else:
        response = f"{command} is not an available command. Be better."
else:
    response = "Usage: python script.py <command> <argument>"
print(f"{response}")

