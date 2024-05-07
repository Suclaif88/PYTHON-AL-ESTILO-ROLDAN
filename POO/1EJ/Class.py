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