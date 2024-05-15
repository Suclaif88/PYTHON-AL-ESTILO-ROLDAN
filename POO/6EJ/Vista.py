import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

while True:
    print("--REGISTRO DE ESTUDIANTE--")
    N = str(input("Ingrese el nombre del estudiante: "))
    Cn = int(input("Ingrese el número de notas del estudiante: "))
    Notas = []
    for i in range(Cn):
        Nt = float(input("Ingrese la nota: "))
        Notas.append(Nt)
    Obj.Registro(N,Notas)
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
