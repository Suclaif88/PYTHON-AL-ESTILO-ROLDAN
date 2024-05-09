import os

os.system("cls")

datos = [
    {"Nombre": "Catalina Durán", "Sexo": "F", "Edad": 29, "Peso": 54, "Talla": 1.57, "IMC": 22, "Categoria": ""},
    {"Nombre": "J. Miguel Contreras", "Sexo": "M", "Edad": 30, "Peso": 75, "Talla": 1.72, "IMC": 25, "Categoria": ""},
    {"Nombre": "Ingrid Herrera", "Sexo": "F", "Edad": 35, "Peso": 80, "Talla": 1.61, "IMC": 31, "Categoria": ""},
    {"Nombre": "Luis Muñoz", "Sexo": "M", "Edad": 26, "Peso": 82, "Talla": 1.67, "IMC": 29, "Categoria": ""},
    {"Nombre": "Pamela Islas", "Sexo": "F", "Edad": 39, "Peso": 90, "Talla": 1.56, "IMC": 37, "Categoria": ""},
    {"Nombre": "Ricardo Flores", "Sexo": "M", "Edad": 29, "Peso": 45, "Talla": 1.57, "IMC": 17, "Categoria": ""},
    {"Nombre": "Lourdes Pérez", "Sexo": "F", "Edad": 39, "Peso": 90, "Talla": 1.56, "IMC": 40, "Categoria": ""}
]

for persona in datos:
    if persona['IMC'] < 18:
        persona['Categoria'] = 'Bajo peso'
    elif 18 <= persona['IMC'] < 25:
        persona['Categoria'] = 'Normal'
    elif 25 <= persona['IMC'] < 30:
        persona['Categoria'] = 'Sobrepeso'
    elif 30 <= persona['IMC'] < 35:
        persona['Categoria'] = 'Morbido I'
    elif 35 <= persona['IMC'] < 40:
        persona['Categoria'] = 'Morbido II'
    else:
        persona['Categoria'] = 'Morbido III'
        
for persona in datos:
    print(f"{persona['Nombre']}: {persona['Categoria']}")