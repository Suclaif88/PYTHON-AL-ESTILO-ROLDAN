class CLASE:
    def __init__(self):
        self.Nombre = input("Ingrese el nombre del estudiante: ")
        self.Notas = []
    def RegistroNotas(self, Nota):
        self.Notas.append(Nota)
            
    def MostrarRegistro(self):
        print(f"El nombre del estudiante es: {self.Nombre}")
        print(f"Las notas del estudiante son: {self.Notas}")

    def Promedio(self):
        suma = 0
        for i in self.Notas:
            suma += i
        promedio = suma / len(self.Notas)
        print(f"El promedio del estudiante es: {promedio}")

    def Aprobado(self):
        suma = 0
        for i in self.Notas:
            suma += i
        promedio = suma / len(self.Notas)
        if promedio >= 5:
            print("El estudiante esta aprobado")
        else:
            print("El estudiante esta reprobado")