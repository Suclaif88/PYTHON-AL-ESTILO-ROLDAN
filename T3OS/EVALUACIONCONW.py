import os

os.system("cls")

No = []
Su = []
D = {}

for i in range(2):
    N = str(input("Ingrese un nombre: "))
    No.append(N)
    S = int(input("Ingrese un sueldo: "))
    
    if N == 'wilson' and S > 1 and S < 300:
        S = S + S * 0.2
        Su.append(S)
    elif N == 'fredy' and S >= 300 and S < 600:
        S = S + S * 0.1
        Su.append(S)
    else:
        Su.append(S)
    
P = sum(Su) / len(Su)
D = dict(zip(No, Su))

print(No)
print(Su)
print(P)
print(D)
