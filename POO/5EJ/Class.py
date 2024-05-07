class CLASE:
    def __init__(self):
        self.Notas = []
        
    def imp(self):
        print(self.Notas)
        
    def IngresoDatos(self):
        notas_ganadas = []
        notas_perdidas = []

        for i in range(1, 3):
            print("----------------------------")
            Nota = float(input(f"Ingrese la nota {i}: "))
            sexo = input(f"Ingrese el sexo {i}: ")
            ganadas, perdidas = self.procesar_nota(Nota, sexo)
            notas_ganadas.extend(ganadas)
            notas_perdidas.extend(perdidas)

        promedio_ganadas = self.calcular_promedio(notas_ganadas)
        promedio_perdidas = self.calcular_promedio(notas_perdidas)

        print("----------------------------")
        print(f"Promedio de notas ganadas: {promedio_ganadas}")
        print(f"Promedio de notas perdidas: {promedio_perdidas}")

        print("Cantidad de notas ganadas:", len(notas_ganadas))
        print("Cantidad de notas perdidas:", len(notas_perdidas))

    def procesar_nota(self, nota, sexo):
        ganadas = []
        perdidas = []
        if sexo.lower() == "mujer":
            nota -= 3
            perdidas.append(nota)
        elif sexo.lower() == "hombre":
            nota += 2
            ganadas.append(nota)
        else:
            print("Sexo no reconocido. La nota se registrará sin modificar.")
            self.Notas.append(nota)
        return ganadas, perdidas

    def calcular_promedio(self, notas):
        return sum(notas) / len(notas) if notas else 0