import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

for i in range(1,11):
    print("----------------------------")
    Nombre = input(f"Ingrese el nombre {i}: ")
    Precio = int(input(f"Ingrese el precio {i}: "))
    Obj.Registro(Nombre,Precio)


Obj.PromedioPrecio()
Obj.TotalPrecio()
Obj.PrecioMayor()
Obj.PrecioMenor()

# Obj.Mostrar()