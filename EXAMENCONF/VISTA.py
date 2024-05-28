import os
from CLASE import CLASE

os.system("cls")

Obj = CLASE() 

for i in range(1,5):
    S = float(input(f"INGRESE EL SUELDO {i}: "))
    E = int(input(f"INGRESE LA EDAD {i}: "))
    N = float(input(f"INGRESE LA NOTA {i}: "))
    Obj.IngresoDatos(S,E,N)
    os.system("cls")

#-----------Impresion--------------------------------

os.system("cls")

Obj.IMPRIMIR()
