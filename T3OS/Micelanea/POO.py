# class Persona:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# p1 = Persona("Jhon", 36) #instanciar objetos
# print(p1.name)
# print(p1.age)

class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def Imprimir(self):
        print(f"El nombre es {self.nombre} y su sueldo es: {self.sueldo}")
    def CalcularSueldo(self):
        if self.sueldo > 3000:
            print("Paga impuestos")
        else:
            pass
        

nombre = input("Ingrese el nombre: ")
sueldo = int(input("Ingrese el sueldo: "))

p1 = Empleado(nombre, sueldo) #instanciar objetos
p1.Imprimir()
p1.CalcularSueldo()