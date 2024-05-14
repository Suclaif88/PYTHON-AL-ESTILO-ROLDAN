class CLASE:
    def __init__(self):
        self.Sueldos = []
        
    def AgregarSueldo(self, sueldo):
        self.Sueldos.append(sueldo)
         
    def Promedio(self):
        self.Promedio = sum(self.Sueldos) / len(self.Sueldos)
        print(f"El promedio es: {self.Promedio}")

    def Mayor(self):
        Mayor = max(self.Sueldos)
        print(f"El mayor es: {Mayor}")

    def Menor(self):
        Menor = min(self.Sueldos)
        print(f"El menor es: {Menor}")

    def Estado(self):
        if self.Promedio >= 1 and self.Promedio <= 4000000:
            print("Sueldo basico")
        elif self.Promedio <= 0:
            print("Sueldo basico")
        elif self.Promedio >= 4000001 and self.Promedio <= 10000000:
            print("Sueldo medio")
        elif self.Promedio >= 10000001 and self.Promedio <= 20000000:
            print("Sueldo alto")
        else:
            print("Sueldo alto")
        
    def Imp(self):
        print(self.Sueldos)
        
        