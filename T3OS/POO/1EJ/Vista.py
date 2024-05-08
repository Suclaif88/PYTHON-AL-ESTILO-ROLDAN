from Class import Empleado


nombre = input("Ingrese el nombre: ")
sueldo = int(input("Ingrese el sueldo: "))

p1 = Empleado(nombre, sueldo) #instanciar objetos
p1.Imprimir()
p1.CalcularSueldo()