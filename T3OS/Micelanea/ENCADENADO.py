import os

os.system("cls")

cadena = input("Ingrese una cadena: ")
cadena = cadena.lower()

if cadena == cadena[::-1]:
    print("La cadena es un palindromo")
else:
    print("La cadena no es un palindromo")

print("Longitud de la cadena:",len(cadena))

print("Cadena invertida:",cadena[::-1])

V = []

for C in cadena:
    if C.lower() in ['a', 'e', 'i', 'o', 'u']:
        V.append(C)

print("Vocales:",len(V))

replace = input("Ingrese subcadena: ")
cadena = cadena.replace(cadena, replace)

print("Cadena reemplazada:",cadena)

input()

os.system("cls")

T1 = (1, "manzana", 2.5)
T2 = (5, "Mango", 4.5)

T3 = T1 + T2

print("Tuplas sumadas:",T3)
print("Tupla contada:",len(T3))

T4 = ("Pedro","Pablo","Jacinto","Jose","Humberto","Humberto")

print(T4[0],T4[4])

print(T4[2:])

element_count = {}

for element in T4:
    if element not in element_count:
        element_count[element] = 1
    else:
        element_count[element] += 1

print(element_count)