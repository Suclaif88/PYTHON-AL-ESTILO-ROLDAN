import os

class CLASE:
    def __init__(self):
        self.Estudiantes = {}
        self.Aprobados = 0
        self.Reprobados = 0 
        self.Total_Promedio = 0
    
    def Registro(self):
        while True:
            print("--REGISTRO DE ESTUDIANTE--")
            N = str(input("Ingrese el nombre del estudiante: "))
            Cn = int(input("Ingrese el número de notas del estudiante: "))
            Notas = []
    
            for _ in range(Cn): # se puede definir un ciclo for sin iterador
                Nt = float(input("Ingrese la nota: "))
                Notas.append(Nt)
        
            Promedio = sum(Notas) / len(Notas)
            self.Total_Promedio += Promedio
    
            self.Estudiantes[N] = Notas
    
            Acc = input("¿DESEA HACER UN NUEVO REGISTRO DE ESTUDIANTE? Y/N: ")
            if Acc.upper() == "Y":
                os.system("cls")
                pass
            elif Acc.upper() == "N":
                break
            else:
                print("OPCIÓN NO VÁLIDA")
                break
            
    def DefinirPromedio(self):
        for nombre in self.Estudiantes:
            notas = self.Estudiantes[nombre]
            Promedio = sum(notas) / len(notas)
            if Promedio >= 3.0 and Promedio <= 5.0:
                self.Aprobados += 1
            elif Promedio >= 1.0 and Promedio <= 2.9:
                self.Reprobados += 1
                
    def Impresion(self):
        os.system("cls")
        print("Estudiantes que Perdieron:", self.Reprobados)
        print("Estudiantes que Ganaron:", self.Aprobados)
        
        for nombre in self.Estudiantes:
            notas = self.Estudiantes[nombre]
            Promedio = sum(notas) / len(notas)
            print(f"El estudiante {nombre} tiene un promedio: {Promedio}")
    
        print(f"Promedio total de notas: {self.Total_Promedio / len(self.Estudiantes)}")
 
        for x,y in self.Estudiantes.items():
            print(f"El estudiante {x} tiene las notas: {y}")

        print(f"El diccionario completo es: {self.Estudiantes}")
        
#SRD
