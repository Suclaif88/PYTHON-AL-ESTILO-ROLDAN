import os
os.system("cls")

L =  [8,6,4,2,3]
L1 = [5,7,10,12,11]
L2 = [4,6,3,5,8]
L3 = [6,9,10,13,17]
L4 = [5,7,9,6,4]

P = []
I = []

for i in L,L1,L2,L3,L4:
    for j in i:
     if isinstance(j,int) and j % 2 == 0:
         P.append(j)
     else:
         I.append(j)

Suma_P = sum(P)
Suma_I = sum(I)

print("La suma de los pares es:",Suma_P)
print("La suma de los impares es:",Suma_I)

print("Hay",len(P),"PARES")
print("Hay",len(I),"IMPARES")

diagonal = L[0] + L1[1] + L2[2] + L3[3] + L4[4]
diagonal2 = L4[0] + L3[1] + L2[2] + L1[3] + L[4]

print("Diagonal principal:",diagonal)
print("Diagonal secundaria:",diagonal2)