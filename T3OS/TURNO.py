import os

os.system("cls")

Empleados = [
    {"NOMBRE": "Nora", "APELLIDO": "Rodríguez", "TURNO": "M", "SUELDO": 7500, "SECCIÓN": 1,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Rafaela", "APELLIDO": "Martínez", "TURNO": "M", "SUELDO": 6800, "SECCIÓN": 4,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Mikaela", "APELLIDO": "Antón", "TURNO": "T", "SUELDO": 4500, "SECCIÓN": 2,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Mariana", "APELLIDO": "Mendoza", "TURNO": "M", "SUELDO": 7000, "SECCIÓN": 1,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Gonzalo", "APELLIDO": "Casío", "TURNO": "N", "SUELDO": 9340, "SECCIÓN": 1,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "José", "APELLIDO": "Meza", "TURNO": "N", "SUELDO": 7800, "SECCIÓN": 3,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Bruno", "APELLIDO": "Morán", "TURNO": "M", "SUELDO": 5400, "SECCIÓN": 4,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Renzo", "APELLIDO": "Alcántara", "TURNO": "M", "SUELDO": 5000, "SECCIÓN": 1,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Denisse", "APELLIDO": "Peñafiel", "TURNO": "T", "SUELDO": 42000, "SECCIÓN": 2,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Ricardo", "APELLIDO": "Juárez", "TURNO": "M", "SUELDO": 11000, "SECCIÓN": 2,"VERDADERO_O_FALSO":"","SITUACION":""},
    {"NOMBRE": "Andrés", "APELLIDO": "Toledo", "TURNO": "T", "SUELDO": 8200, "SECCIÓN": 1,"VERDADERO_O_FALSO":"","SITUACION":""}
]

for persona in Empleados:
    if persona['TURNO'] == 'M':
        if persona['SUELDO'] <= 7000 or persona['SECCIÓN'] == 4:
            persona['VERDADERO_O_FALSO'] = 'Verdadero'
        else:
            persona['VERDADERO_O_FALSO'] = 'Falso'
    else:
        persona['VERDADERO_O_FALSO'] = 'Falso'
for persona in Empleados:
    if persona['VERDADERO_O_FALSO'] == 'Verdadero':
        persona['SITUACION'] = 'Promovido'
    else:
        persona['SITUACION'] = 'No promovido'
    print(f"{persona['TURNO']}:{persona['SUELDO']}:{persona['SECCIÓN']}: {persona['VERDADERO_O_FALSO']}: {persona['SITUACION']}")