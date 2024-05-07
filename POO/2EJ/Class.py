class CLASE:
    def __init__(self):
        self.Sueldos = []
    def IngresoDatos(self):
        for i in range(1,6):
            Sueldo = int(input(f"Ingrese el sueldo {i}: "))
            self.Sueldos.append(Sueldo)
            
    def Promedio(self):
        print(f"El promedio es: {sum(self.Sueldos) / len(self.Sueldos)}")

    def Mayor(self):
        Mayor = max(self.Sueldos)
        print(f"El mayor es: {Mayor}")

    def Menor(self):
        Menor = min(self.Sueldos)
        print(f"El menor es: {Menor}")

    def Estado(self):
        Promedio = sum(self.Sueldos) / len(self.Sueldos)
        if Promedio >= 1 and Promedio <= 4000000:
            print("Sueldo basico")
        elif Promedio <= 0:
            print("Sueldo basico")
        elif Promedio >= 4000001 and Promedio <= 10000000:
            print("Sueldo medio")
        elif Promedio >= 10000001 and Promedio <= 20000000:
            print("Sueldo alto")
        else:
            print("Sueldo alto")
        
        