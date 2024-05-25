from Persona import Persona
class Asesor(Persona):
    def __init__(self,apellido,tel,correo,direccion):
        self.apellido = apellido
        self.tel = tel
        Persona.__init__(self,correo,direccion)
        
        
    def Imprimir2(self):
        print(f"El apellido es: {self.apellido} El telefono es: {self.tel} El correo es: {self.correo} La direccion es: {self.direccion}")