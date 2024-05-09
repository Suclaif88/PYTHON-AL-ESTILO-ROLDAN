import os 

os.system("cls")

try:
    N = int(input("Ingrese un numero: "))
    
except ValueError as e:
    print(f"Ingrese un numero correcto: {e}")