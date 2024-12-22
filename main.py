import os
import time
from cryptography.fernet import Fernet

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

while True:
    gen = Fernet.generate_key()
    key = gen.decode()
    print(f"Key : {key}")
    time.sleep(0.1)
