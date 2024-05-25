import os 

os.system("cls")

M1  = [1250,1258,1320,1380,1238]

M2 = [1380,2050,1250,1560,1258]

M3 = []

for i in M1:
 for j in M2:
  if i == j:
    M3.append(i)
    
print(M3)