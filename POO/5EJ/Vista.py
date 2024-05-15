import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

for i in range(1,3):
    print("----------------------------")
    Nota = float(input(f"Ingrese la nota {i}: "))
    Sexo = input(f"Ingrese el sexo (hombre/mujer): ").lower()
    Obj.IngresoDatos(Nota,Sexo)
    
Obj.ProcesarDatos()

os.system("cls")

Obj.PromediosNotas()
Obj.ContarNotas()
Obj.MinMaxNotas()
# Obj.pr()