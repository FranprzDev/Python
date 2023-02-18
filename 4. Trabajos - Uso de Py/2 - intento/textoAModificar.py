import os

with open("sd.txt", "r") as f:
    for linea in f:
        if 'error' in linea.lower():
            print(linea.strip())
