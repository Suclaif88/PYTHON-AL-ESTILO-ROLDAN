class CLASE:
    def __init__(self):
        self.Dicc = []
        
    def Registro(self):
        for i in range(1,3):
            print("----------------------------")
            Nombre = input(f"Ingrese el nombre {i}: ")
            Precio = int(input(f"Ingrese el precio {i}: "))
            if Precio >= 1 and Precio <= 1000:
                pass
            else:
                print("Precio invalido")
                
            if  Nombre == "susana":
                Precio = Precio * 1.2
                self.Dicc.append({"Nombre":Nombre,"Precio":Precio})
            elif Nombre == "jessica":
                Precio = Precio * 1.15
                self.Dicc.append({"Nombre":Nombre,"Precio":Precio})
            elif Nombre == "Wilson":
                Precio = Precio * 1.1
                self.Dicc.append({"Nombre":Nombre,"Precio":Precio})
            else:
                self.Dicc.append({"Nombre":Nombre,"Precio":Precio})
        print("----------------------------")
            
    def PromedioPrecio(self):
        P = sum(i['Precio'] for i in self.Dicc) / len(self.Dicc)
        print(f"El promedio de los precios es: {P}")

    def TotalPrecio(self):
        T = sum(i['Precio'] for i in self.Dicc)
        print(f"El total de los precios es: {T}")
        
    def PrecioMayor(self):
        P = max(i['Precio'] for i in self.Dicc)
        print(f"El precio mayor es: {P}")
        
    def PrecioMenor(self):
        P = min(i['Precio'] for i in self.Dicc)
        print(f"El precio menor es: {P}")

    # def Mostrar(self):
    #     for i in self.Dicc:
    #         print(f"Nombre: {i['Nombre']}, Precio: {i['Precio']}")
