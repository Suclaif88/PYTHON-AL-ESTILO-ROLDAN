def Numeros(n):
    if n > 0:
        Numeros(n-1)
        print(n)
n=100
Numeros(n)