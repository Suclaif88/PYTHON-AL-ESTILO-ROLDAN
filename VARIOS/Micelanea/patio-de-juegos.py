suma = lambda x,y : x + y #Una funcion anonima

print(suma(5,5))


iterador = iter([1, 2, 3])
while True:
    try:
        print(next(iterador))
    except StopIteration:
        print("No hay más elementos.")
        break



numeros = [1, 2, 3]
iterador = iter(numeros)

while True:
    try:
        numero = next(iterador)
        print(numero)
    except StopIteration:
        break
    

x = 5

y = 0
    
try:
    
    z = x / y
    print(z) 
    

except ZeroDivisionError:
    print("eso no se puede dividir")
    
    
    
    
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(e)




lista = [1, 2, 3, 4, 5]
for elemento in reversed(lista):
    print(elemento)


mi_diccionario = {}  # Crear un diccionario vacío

# Insertar elementos utilizando la sintaxis de indexación

HOLA = 'CLAVE1'

notas = [5,3,2,2] 


mi_diccionario[HOLA] = notas
mi_diccionario['clave2'] = 'valor2'
mi_diccionario['clave3'] = 'valor3'

print(mi_diccionario)


letras = ['a', 'b', 'c']

# Método enumerate() para obtener índices y valores al iterar sobre una lista
for indice, valor in enumerate(letras):
    print(f"Índice: {indice}, Valor: {valor}")
    
def hola(x,y):
    return x + y

print(hola(5,5))


try:
    print ("hola"+'mundo')
    
except SyntaxError:
    print("ERROR DE SINTAX")