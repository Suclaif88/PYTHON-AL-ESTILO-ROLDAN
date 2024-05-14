class CLASE:
    def __init__(self):
        self.Notas = []
        self.NotasG = []
        self.NotasP = []
        
    def IngresoDatos(self):
        for i in range(1,11):
            print("----------------------------")
            Nota = float(input(f"Ingrese la nota {i}: "))
            Sexo = input(f"Ingrese el sexo (hombre/mujer): ")
            if Sexo.lower() == "mujer":
                Nota -= 3.0
                self.Notas.append(Nota)
            elif Sexo.lower() == "hombre":
                Nota += 2.0
                self.Notas.append(Nota)
            else:
                self.Notas.append(Nota)
    
    def ProcesarNotas(self):
        for i in self.Notas:
            if i >= 3.0 and i <= 5.0:
                self.NotasG.append(i)
            else:
                self.NotasP.append(i)
                
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
          
    # def pr(self):
    #     print(f"{self.Notas}")
    #     print(f"{self.NotasG}")
    #     print(f"{self.NotasP}")
            
