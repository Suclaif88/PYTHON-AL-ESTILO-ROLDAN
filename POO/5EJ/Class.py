class CLASE:
    def __init__(self):
        self.Notas = []
        self.NotasG = []
        self.NotasP = []
        
    def IngresoDatos(self, Nota, Sexo):
            if Sexo == "mujer":
                Nota -= 3.0
                self.Notas.append(Nota)
            elif Sexo == "hombre":
                Nota += 2.0
                self.Notas.append(Nota)
            else:
                self.Notas.append(Nota)
                
    def ProcesarDatos(self):
        for i in self.Notas:
            if i >= 5.0:
                self.NotasG.append(i)
            else:
                self.NotasP.append(i)
                
    def PromedioNGanadas(self):
        PG = sum(self.NotasG) / len(self.NotasG)
        print(f"El promedio de notas ganadas es: {PG}")
                  
    def PromedioNPerdida(self):
        PP = sum(self.NotasP) / len(self.NotasP)
        print(f"El promedio de notas perdidas es: {PP}")
        
    def ContarNotasG(self):
        NG = len(self.NotasG)
        print(f"El numero de notas aprobadas es: {NG}")
        
    def ContarNotasP(self):
        NP = len(self.NotasP)
        print(f"El numero de notas reprobadas es: {NP}")
    
    def MinNotas(self):
        MINN = min(self.Notas)
        
        print(f"La nota mas baja es: {MINN}")
        
    def MaxNotas(self):
        MAXN = max(self.Notas)
        print(f"La nota mas alta es: {MAXN}")  
                
    # def pr(self):
    #     print(f"{self.Notas}")
    #     print(f"{self.NotasG}")
    #     print(f"{self.NotasP}")
            
