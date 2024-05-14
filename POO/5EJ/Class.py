class CLASE:
    def __init__(self):
        self.Notas = []
        self.NotasG = []
        self.NotasP = []
        
    def IngresoDatos(self,Nota,Sexo):
            if Sexo == "mujer":
                Nota -= 3.0
                self.Notas.append(Nota)
            elif Sexo == "hombre":
                Nota += 2.0
                self.Notas.append(Nota)
            else:
                self.Notas.append(Nota)
                
                #------arreglar---------------
            # if Nota >= 5.0:
            #     self.NotasG.append(Nota)
            # else:
            #     self.NotasP.append(Nota)
                
            
            
    def PromediosNotas(self):
        PG = sum(self.NotasG) / len(self.NotasG)
        PP = sum(self.NotasP) / len(self.NotasP)
        print(f"El promedio de notas ganadas es: {PG}")
        print(f"El promedio de notas perdidas es: {PP}")
        
    def ContarNotas(self):
        NG = len(self.NotasG)
        NP = len(self.NotasP)
        print(f"El numero de notas aprobadas es: {NG}")
        print(f"El numero de notas reprobadas es: {NP}")
    
    def MinMaxNotas(self):
        MINN = min(self.Notas)
        MAXN = max(self.Notas)
        print(f"La nota mas baja es: {MINN}")
        print(f"La nota mas alta es: {MAXN}")
          
    def pr(self):
        print(f"{self.Notas}")
        print(f"{self.NotasG}")
        print(f"{self.NotasP}")
            
