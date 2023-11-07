from sys import argv
import os

if os.system(f"ping -c 2 {argv[1]} > ./null ") == 0:
    print("UP !")
else:
    print("DOWN !")