import psutil
import socket

def GetWifi():
    for interface, addrs in psutil.net_if_addrs().items():
        if "Wi-Fi" in interface:  
            for addr in addrs:
                if addr.family == 2:  
                    return addr.address

print(GetWifi())