import os
from Class import CLASE

os.system("cls")

Obj = CLASE()

for i in range(1,3):
        print("----------------------------")
        Nombre = input(f"Ingrese el nombre {i}: ").lower()
        while True:
            try:
                Precio = int(input(f"Ingrese el precio {i}: "))
                if 1 <= Precio <= 1000:
                    break
                else:
                    print("Precio invalido. Debe estar entre 1 y 1000.")
            except ValueError:
                    print("Por favor, ingrese un número válido.")
        Obj.Registro(Nombre,Precio)

Obj.PromedioPrecio()
Obj.TotalPrecio()
Obj.PrecioMayor()
Obj.PrecioMenor()

# Obj.Mostrar()