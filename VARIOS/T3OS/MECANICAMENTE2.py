import os

os.system("cls")

M = [[1,1,1,1,1,1,1,1],
     [2,2,2,2,2,2,2,2],
     [0,0,0,0,0,0,0,0],
     [4,4,4,4,4,4,4,4],
     [5,5,5,5,5,5,5,5],
     [6,6,6,6,6,6,6,6],
     [7,7,7,7,7,7,7,7],
     [8,8,8,8,8,8,8,8]]

P = []
I = []
C = []

for i in M:
    for j in i:
     if isinstance(j,int) and j % 2 == 0:
         if j == 0:
             C.append(j)
             j += 1  
         P.append(j)
     else:
         I.append(j)
                 
print("PARES:",len(P))
print("IMPARES:",len(I))
print("CEROS",len(C))