import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

while True:
    print("--REGISTRO DE ESTUDIANTE--")
    N = str(input("Ingrese el nombre del estudiante: "))
    Cn = int(input("Ingrese el número de notas del estudiante: "))
    Notas = []
    Obj.Registro(N,Cn,Notas)
    Acc = input("¿DESEA HACER UN NUEVO REGISTRO DE ESTUDIANTE? Y/N: ")
    if Acc.upper() == "Y":
        os.system("cls")
        pass
    elif Acc.upper() == "N":
        break
    else:
        print("OPCIÓN NO VÁLIDA")
        break


Obj.DefinirPromedio()
Obj.Impresion()

#SRD
