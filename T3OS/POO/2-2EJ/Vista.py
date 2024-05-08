import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

for i in range(1, 6):
    Sueldo = int(input(f"Ingrese el sueldo {i}: "))
    Obj.AgregarSueldo(Sueldo)

os.system("cls")

Obj.Promedio()
Obj.Mayor()
Obj.Menor()
Obj.Estado()
Obj.Imp()
