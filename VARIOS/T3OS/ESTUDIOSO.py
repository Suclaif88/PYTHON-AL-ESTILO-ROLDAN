import os

os.system("cls")

Estudiantes = {}
Aprobados = 0
Reprobados = 0 
Total_Promedio = 0

while True:
    print("--REGISTRO DE ESTUDIANTE--")
    N = str(input("Ingrese el nombre del estudiante: "))
    Cn = int(input("Ingrese el numero de notas del estudiante: "))
    Notas = []
    
    for i in range(Cn):
        Nt = float(input("Ingrese la nota: "))
        Notas.append(Nt)
        
    Promedio = sum(Notas)/len(Notas)
    Total_Promedio += Promedio
    
    Estudiantes[N] = Notas
    
    Acc = input("¿DESEA HACER UN NUEVO REGISTRO DE ESTUDIANTE? Y/N: ")
    if Acc.upper() == "Y":
        os.system("cls")
        pass
    elif Acc.upper() == "N":
        break
    else:
        print("OPCION NO VALIDA")
        break

for nombre in Estudiantes:
    notas = Estudiantes[nombre]
    Promedio = sum(notas) / len(notas)
    if Promedio >= 3.0 and Promedio <= 5.0:
        Aprobados += 1
    elif Promedio >= 1.0 and Promedio <= 2.9:
        Reprobados += 1
        
#--ZONA-DE-IMPRESION-------------------------------------------
os.system("cls")

print("Estudiantes que Ganaron:", Aprobados)
print("Estudiantes que Perdieron:", Reprobados)

for nombre in Estudiantes:
    notas = Estudiantes[nombre]
    Promedio = sum(notas) / len(notas)
    print(f"El estudiante {nombre} tiene un promedio: {Promedio}")
    
print(f"Promedio General Total: {Total_Promedio / len(Estudiantes)}")
 
for x,y in Estudiantes.items():
    print(f"El estudiante {x} tiene las notas: {y}")

print(f"El diccionario completo es: {Estudiantes}")

#SRD
