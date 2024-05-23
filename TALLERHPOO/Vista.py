import os
from Empleado import Empleado

os.system("cls")

nombre = input("INGRESE SU NOMBRE: ")
apellido = input("INGRESE SU APELLIDO: ")
celular = input("INGRESE SU CELULAR: ")
tel = input("INGRESE SU TELEFONO: ")
correo = input("INGRESE SU CORREO: ")
direccion = input("INGRESE SU DIRECCION: ")

os.system("cls")

Obj = Empleado(nombre,apellido,celular,tel,correo,direccion)

Acc = int(input("SELECCIONE ROL 1.ASESOR / 2.EMPLEADO: "))

if Acc == 1:
    print("ASESOR")
    Obj.Imprimir2()
elif Acc == 2:
    print("EMPLEADO")
    Obj.Imprimir()
else:
    print("ERROR")

