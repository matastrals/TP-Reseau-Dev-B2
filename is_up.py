from sys import argv
import os

if os.system(f"ping {argv[1]} > ./null ") == 0:
    print("UP !")
else:
    print("DOWN !")