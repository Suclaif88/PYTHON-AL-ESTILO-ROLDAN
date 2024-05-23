from HERENCIA2 import empleado

nombre = input()
apellido = input()
telefono = input()
direccion = input()

Obj = empleado()

Obj.datos(direccion,telefono,nombre,apellido)
Obj.imprimir()
