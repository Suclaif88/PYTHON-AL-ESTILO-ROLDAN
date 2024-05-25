from Asesor import Asesor
class Empleado(Asesor):
    
    def __init__(self,nombre,apellido,celular,tel,correo,direccion):
        self.celular = celular
        self.nombre = nombre
        Asesor.__init__(self,apellido,tel,correo,direccion)
        
    
    def Imprimir(self):
        print(f"El nombre es: {self.nombre} El celular es: {self.celular}")
        Asesor.Imprimir2(self)
        
    def Rol(self,Acc):
        if Acc == 1:
            print("ASESOR")
            self.Imprimir2()
        elif Acc == 2:
            print("EMPLEADO")
            self.Imprimir()  