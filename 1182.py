coluna = int(input())
op = str(input())
matriz=[]
for i in range(0,12):
    matriz.append([])
    for j in range(0,12):
        matriz[i].append(float(input()))
soma=0
for i in range(0,12):
    soma+=matriz[i][coluna]
if(op=="S"):
    print("%.1f"%soma)
elif(op=="M"):
    print("%.1f"%(soma/12))