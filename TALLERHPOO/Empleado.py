from Asesor import Asesor
class Empleado(Asesor):
    
    def __init__(self,nombre,apellido,celular,tel,correo,direccion):
        self.celular = celular
        self.nombre = nombre
        Asesor.__init__(self,apellido,tel,correo,direccion)
        
    
    def Imprimir(self):
        print(f"El nombre es: {self.nombre} El celular es: {self.celular}")
        Asesor.Imprimir2(self)