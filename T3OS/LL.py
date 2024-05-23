import os

os.system("cls")

Lista = []
ListaC = []
ListaB = []

A = None

while A != 99:
 A = int(input("Ingrese un numero: "))
 if A == 99:
     break
 else:
     Lista.append(A)
     ListaC.append(A)
     ListaB.append(A)
    
 os.system("cls")

 for i in range(len(Lista)):
    for j in range(len(Lista)- 1):
        if Lista[j] > Lista[j + 1]:
            Lista[j], Lista[j + 1] = Lista[j + 1], Lista[j]
            
 for i in range(len(ListaB)):
    for j in range(len(ListaB)- 1):
        if ListaB[j] < ListaB[j + 1]:
            ListaB[j], ListaB[j + 1] = ListaB[j + 1], ListaB[j]
    os.system("cls")
    
    print("Lista original: ",ListaC)
    
    print("Lista ordenada menor mayor",Lista)
    
    print("Lista ordenada mayor menor ",ListaB)
