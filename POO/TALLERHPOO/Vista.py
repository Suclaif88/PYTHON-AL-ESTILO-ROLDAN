import os
from Empleado import Empleado

os.system("cls")

Acc = int(input("SELECCIONE ROL 1.ASESOR / 2.EMPLEADO: "))

if Acc in [1,2]:
    apellido = input("INGRESE SU APELLIDO: ")
    tel = input("INGRESE SU TELEFONO: ")
    correo = input("INGRESE SU CORREO: ")
    direccion = input("INGRESE SU DIRECCION: ")
    if Acc == 2:
        nombre = input("INGRESE SU NOMBRE: ")
        celular = input("INGRESE SU CELULAR: ")
    else:
        nombre = None
        celular = None
else:
    print("ROL INCORRECTO")    

os.system("cls")

Obj = Empleado(nombre,apellido,celular,tel,correo,direccion)

Obj.Rol(Acc)

