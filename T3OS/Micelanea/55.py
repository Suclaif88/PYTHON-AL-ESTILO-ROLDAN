import os

os.system("cls")


M = [[3,1,1,1,8],
     [2,2,2,2,2],
     [3,3,3,3,3],
     [4,4,4,4,4],
     [7,5,5,5,0],]
         
for i in range(5):
    for j in range(5):
        print(M[i][j],end=" ")
    print()

fila_sums = [sum(row) for row in M]
columna_sums = [sum(col) for col in zip(*M)]

print("Suma de filas:", fila_sums)
print("Suma de columna:", columna_sums)