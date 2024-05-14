import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

for i in range(1,7):
    Nota = int(input(f"Ingrese la nota {i}: "))
    Obj.RegistroNotas(Nota)

os.system("cls")

Obj.MostrarRegistro()
Obj.Promedio()
Obj.Aprobado()