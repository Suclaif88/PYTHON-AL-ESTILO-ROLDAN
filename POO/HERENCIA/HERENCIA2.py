from HERENCIA import persona
class empleado(persona):
    
    def datos(self,direccion,telefono,nombre,apellido):
        self.direccion = direccion
        self.telefono = telefono
        persona.datos(self,nombre,apellido)
    
    def imprimir(self):
        print(f"{self.nombre,self.apellido,self.direccion,self.telefono}")