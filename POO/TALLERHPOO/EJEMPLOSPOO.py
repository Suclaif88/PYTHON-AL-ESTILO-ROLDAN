#ENCAPSULAMIENTO

class Taza:
    def __init__(self, color, material):
        self._color = color  # Atributo protegido
        self.__material = material  # Atributo privado

    def mostrar_color(self):
        return self._color

    def __mostrar_material(self):  # Método privado
        return self.__material

# Crear una instancia de la clase Taza
mi_taza = Taza("Rojo", "Cerámica")

# Acceder al color (atributo protegido)
print(mi_taza.mostrar_color())  # Output: Rojo

# Acceder al material (atributo privado)
# Esto lanzará un error ya que el atributo es privado
# print(mi_taza.__material)
# Sin embargo, podemos acceder al método que devuelve el material
# print(mi_taza.__mostrar_material())

#HERENCIA

class TazaGrande(Taza):
    def __init__(self, color, material, capacidad):
        super().__init__(color, material)
        self.capacidad = capacidad

    def mostrar_capacidad(self):
        return self.capacidad

# Crear una instancia de la clase TazaGrande
mi_taza_grande = TazaGrande("Azul", "Porcelana", 500)

# Acceder al color (heredado)
print(mi_taza_grande.mostrar_color())  # Output: Azul

# Acceder a la capacidad (atributo propio)
print(mi_taza_grande.mostrar_capacidad())  # Output: 500

#POLIMORFISMO

class TazaPequeña(Taza):
    def __init__(self, color, material, forma):
        super().__init__(color, material)
        self.forma = forma

    def mostrar_forma(self):
        return self.forma

    # Polimorfismo: método mostrar_color modificado
    def mostrar_color(self):
        return f"La taza {self._color} es pequeña"

# Crear una instancia de la clase TazaPequeña
mi_taza_pequeña = TazaPequeña("Verde", "Plástico", "Circular")

# Acceder al color (heredado pero con polimorfismo)
print(mi_taza_pequeña.mostrar_color())  # Output: La taza Verde es pequeña

#ABSTRACCION

from abc import ABC, abstractmethod

class TazaAbstracta(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def mostrar_tipo(self):
        pass

class TazaCafe(TazaAbstracta):
    def mostrar_tipo(self):
        return "Esta es una taza de café"

# Crear una instancia de la clase TazaCafe
mi_taza_cafe = TazaCafe("Negro")

# Acceder al tipo de taza (abstracción)
print(mi_taza_cafe.mostrar_tipo())  # Output: Esta es una taza de café
