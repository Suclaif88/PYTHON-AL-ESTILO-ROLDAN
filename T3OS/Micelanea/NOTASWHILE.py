import os

os.system("cls")

A = []
R = []
i = 0
os.system("cls")

while True:
    NN = float(input("INGRESE LA NOTA: "))
    if NN >= 3.0 and NN <= 5.0:
        A.append(NN)
        i += 1
    elif NN >= 1.0 and  NN <= 2.9:
        R.append(NN)
        i += 1
    else:
        print("LA NOTA NO ES VALIDA")
    N = str(input("¿DESEA CONTINUAR REGISTRANDO? Y/N: "))
    if N.upper() == 'Y':
        pass
    else:
        break

PA = sum(A) / len(A) if A else 0
PR = sum(R) / len(R) if R else 0
PG = sum(A + R) / i if i > 0 else 0

print(f"LAS NOTAS APROBADAS SON: {A}")
print(f"LAS NOTAS REPROBADAS SON: {R}")
print(f"EL PROMEDIO DE LAS NOTAS APROBADAS ES: {PA:.2f}")
print(f"EL PROMEDIO DE LAS NOTAS REPROBADAS ES: {PR:.2f}")
print(f"EL PROMEDIO GENERAL ES: {PG:.2f}")

if PG >= 3.0:
    print("APROBADO")
else:
    print("REPROBADO")
