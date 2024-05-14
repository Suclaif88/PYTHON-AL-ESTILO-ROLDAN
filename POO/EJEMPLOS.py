# Estructuras de control:

# If-else
x = 10
if x > 0:
    print("x es positivo")
elif x < 0:
    print("x es negativo")
else:
    print("x es cero")

# Bucle For
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Bucle While
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Manejo de excepciones (try-except)
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Métodos comunes:

# Método append() para listas
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Output: [1, 2, 3, 4]

# Método upper() para cadenas de texto
texto = "hola mundo"
texto_en_mayusculas = texto.upper()
print(texto_en_mayusculas)  # Output: "HOLA MUNDO"

# Método keys() para diccionarios
diccionario = {"a": 1, "b": 2, "c": 3}
claves = diccionario.keys()
print(claves)  # Output: dict_keys(['a', 'b', 'c'])

# Método split() para cadenas de texto
texto = "Hola cómo estás"
palabras = texto.split()
print(palabras)  # Output: ['Hola', 'cómo', 'estás']

# Método format() para formatear cadenas
nombre = "Juan"
edad = 30
mensaje = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Output: "Hola, me llamo Juan y tengo 30 años."

# Método join() para concatenar cadenas de texto
lista_de_palabras = ["Hola", "cómo", "estás"]
texto = " ".join(lista_de_palabras)
print(texto)  # Output: "Hola cómo estás"

# Método replace() para reemplazar texto en una cadena
mensaje = "Hola mundo"
nuevo_mensaje = mensaje.replace("mundo", "Python")
print(nuevo_mensaje)  # Output: "Hola Python"

# Método sort() para ordenar listas
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numeros.sort()
print(numeros)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# Método reverse() para invertir el orden de una lista
numeros.reverse()
print(numeros)  # Output: [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]

# Método pop() para eliminar y devolver el último elemento de una lista
ultimo_elemento = numeros.pop()
print(ultimo_elemento)  # Output: 1
print(numeros)  # Output: [9, 6, 5, 5, 4, 3, 3, 2, 1]

# Método len() para obtener la longitud de una lista
longitud = len(numeros)
print(longitud)  # Output: 9

# Método strip() para eliminar espacios en blanco al principio y al final de una cadena
texto = "    Hola    "
texto_limpio = texto.strip()
print(texto_limpio)  # Output: "Hola"

# Método count() para contar ocurrencias de un elemento en una lista
numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
conteo = numeros.count(1)
print(conteo)  # Output: 2

# Método extend() para agregar elementos de una lista a otra lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # Output: [1, 2, 3, 4, 5, 6]

# Método index() para encontrar el índice de un elemento en una lista
indice = lista1.index(3)
print(indice)  # Output: 2

# Método min() para encontrar el elemento más pequeño en una lista
minimo = min(lista1)
print(minimo)  # Output: 1

# Método max() para encontrar el elemento más grande en una lista
maximo = max(lista1)
print(maximo)  # Output: 6

# Método any() para verificar si al menos un elemento de una lista es verdadero
lista_verdadero_falso = [False, True, False]
resultado = any(lista_verdadero_falso)
print(resultado)  # Output: True

# Método all() para verificar si todos los elementos de una lista son verdaderos
resultado = all(lista_verdadero_falso)
print(resultado)  # Output: False

# Método zip() para combinar dos o más listas en tuplas
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
combinado = list(zip(numeros, letras))
print(combinado)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Método enumerate() para obtener índices y valores al iterar sobre una lista
for indice, valor in enumerate(letras):
    print(f"Índice: {indice}, Valor: {valor}")

# Método round() para redondear un número
numero_decimal = 3.14159
numero_redondeado = round(numero_decimal, 2)
print(numero_redondeado)  # Output: 3.14

# Método map() para aplicar una función a cada elemento de una lista
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
resultado = list(map(cuadrado, numeros))
print(resultado)  # Output: [1, 4, 9, 16, 25]
