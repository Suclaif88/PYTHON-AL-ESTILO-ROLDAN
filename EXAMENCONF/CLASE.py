class CLASE:
    
    def __init__(self):
       self.sueldos = []
       self.edades = []
       self.notas = []
       
       self.Ng = []
       self.Np = []
    
    def IngresoDatos(self,S,E,N):
        self.sueldos.append(S)
        self.edades.append(E)
        self.notas.append(N)
        
    def Ganaron(self):
        for _ in self.notas:
            if _ >= 6:
                self.Ng.append(_)
            else:
                pass
        return len(self.Ng)
    
    def Perdieron(self):
        for _ in self.notas:
            if _ <= 5:
                self.Np.append(_)
            else:
                pass
        return len(self.Np)
        
    def PromedioNotas(self):
        return sum(self.notas) / len(self.notas)
        
    def ContarSueldoMayor(self):
        M = 0
        for _ in self.sueldos:
            if _ > 450:
                M = M+1
            else:
                pass
        return M
        
    def ContarSueldoMenor(self):
        Me = 0
        for _ in self.sueldos:
            if _ < 449:
                Me = Me+1
            else:
                pass
        return Me
        
    def SueldoMayor(self):
        return max(self.sueldos)
        
    def SueldoMenor(self):
        return min(self.sueldos)
        
    def PromedioSueldos(self):
        return sum(self.sueldos) / len(self.sueldos)
        
    def EdadMayor(self):
        return max(self.edades)
        
    def EdadMenor(self):
        return min(self.edades)
        
    def CuantosMayoresEdad(self):
        Mayores = 0
        for _ in self.edades:
            if _ >= 18:
                Mayores = Mayores+1
            else:
                pass
        return Mayores
    
    def CuantosMenoresEdad(self):
        Menores = 0
        for _ in self.edades:
            if _ < 18:
                Menores = Menores+1
            else:
                pass
        return Menores
            
    def IMPRIMIR(self):
        
        print(f"GANARON NOTA: {self.Ganaron()}")
        print(f"PERDIERON NOTA: {self.Perdieron()}")

        print(f"EL PROMEDIO DE LAS NOTAS ES: {self.PromedioNotas()}")

        print(f"LA CANTIDAD DE SUELDOS MAYORES ES: {self.ContarSueldoMayor()}")
        print(f"LA CANTIDAD DE SUELDOS MENORES ES: {self.ContarSueldoMenor()}")

        print(f"EL SUELDO MAYOR ES: {self.SueldoMayor()}")
        print(f"EL SUELDO MENOR ES: {self.SueldoMenor()}")
        print(f"EL PROMEDIO DE SUELDOS ES: {self.PromedioSueldos()}")

        print(f"LA EDAD MAYOR ES: {self.EdadMayor()}")
        print(f"LA EDAD MENOR ES: {self.EdadMenor()}")
        print(f"SON MAYORES DE EDAD: {self.CuantosMayoresEdad()}")
        print(f"SON MENORES DE EDAD: {self.CuantosMenoresEdad()}")        
