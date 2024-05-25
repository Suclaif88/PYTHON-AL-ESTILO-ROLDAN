import os
os.system("cls")

L =  [10,10,10,10,10]
L1 = [20,20,20,20,20]
L2 = [30,30,30,30,30]
L3 = [40,40,40,40,40]
L4 = [50,50,50,50,50]

sumas = []


for lista in [L,L1,L2,L3,L4]:
    suma = 0
    for i in lista:
        suma += i
    sumas.append(suma)
suma = 0

for i in sumas:
    suma += i
    
print("Suma de cada fila:",sumas)
print("Suma de las filas:",suma)

sumas = []

for i in range(len(L)):
    column_total = 0
    for lista in [L,L1,L2,L3,L4]:
        column_total += lista[i]
    sumas.append(column_total)
    
suma = 0

for i in sumas:
    suma += i

print("Suma de cada columna:",sumas)
print("Suma de las columnas:",suma)

diagonal = L[0] + L1[1] + L2[2] + L3[3] + L4[4]
diagonal2 = L4[0] + L3[1] + L2[2] + L1[3] + L[4]

print("Diagonal principal:",diagonal)
print("Diagonal secundaria:",diagonal2)