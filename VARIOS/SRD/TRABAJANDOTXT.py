import os

os.system("cls")

for i in range(2):
    s = open("TXT/Prueba.txt", "w")
    s.write(input())
    s = open("TXT/Prueba.txt", "r")
    print(s.read())
    s.close()
    T = input("Ingrese 99 para terminar:")
    if T == "99":
        break