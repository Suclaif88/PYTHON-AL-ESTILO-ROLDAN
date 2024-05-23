import os

os.system("cls")

A = []
R = []

N = int(input("INGRESE EL NUMERO DE NOTAS A REGISTRAR: " ))

os.system("cls")

for i in range(N):
    NN = float(input("INGRESE LA NOTA: "))
    if NN >= 3.0:
        A.append(NN)
    elif NN > 5.0:
        print("ESA NOTA NO ES VALIDA")
    else:
        R.append(NN)


PA = sum(A) / len(A) if A else 0
PR = sum(R) / len(R) if R else 0
PG = sum(A + R) / N if N > 0 else 0

print(f"LAS NOTAS APROBADAS SON:{A}")
print(f"LAS NOTAS REPROBADAS SON:{R}")
print(f"EL PROMEDIO DE LAS NOTAS APROBADAS ES: {PA:.2f}")
print(f"EL PROMEDIO DE LAS NOTAS REPROBADAS ES: {PR:.2f}")
print(f"EL PROMEDIO GENERAL ES:{PG:.2f}")

if PG >= 3.0:
    print("APROBADO")
else:
    print("REPROBADO")
