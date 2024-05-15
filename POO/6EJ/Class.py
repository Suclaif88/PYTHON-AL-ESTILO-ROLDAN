class CLASE:
    def __init__(self):
        self.Estudiantes = {}
        self.Aprobados = 0
        self.Reprobados = 0 
        self.Total_Promedio = 0
    
    def Registro(self,N,Notas):
            Promedio = sum(Notas) / len(Notas)
            self.Total_Promedio += Promedio
            self.Estudiantes[N] = Notas
            
    def DefinirPromedio(self):
        for nombre in self.Estudiantes:
            notas = self.Estudiantes[nombre]
            Promedio = sum(notas) / len(notas)
            if Promedio >= 3.0 and Promedio <= 5.0:
                self.Aprobados += 1
            elif Promedio >= 1.0 and Promedio <= 2.9:
                self.Reprobados += 1
           
    def MostrarEAprovados(self):
        print("Estudiantes que Ganaron:", self.Aprobados)     
           
    def MostrarEReprobados(self):
        print("Estudiantes que Perdieron:", self.Reprobados)
    
    def MostrarEConPromedio(self):
        for nombre in self.Estudiantes:
            notas = self.Estudiantes[nombre]
            Promedio = sum(notas) / len(notas)
            print(f"El estudiante {nombre} tiene un promedio: {Promedio}")
        
    def MostrarPTotal(self):
        print(f"Promedio total de notas: {self.Total_Promedio / len(self.Estudiantes)}")    
        
    def MostrarEConNotas(self):
        for x,y in self.Estudiantes.items():
            print(f"El estudiante {x} tiene las notas: {y}")
            
    def MostrarDiccionario(self):
        print(f"El diccionario completo es: {self.Estudiantes}")
            
#SRD
