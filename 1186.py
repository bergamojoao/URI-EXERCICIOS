matriz=[]
op=input()
for i in range(0,12):
    sub = []
    for j in range(0,12):
        sub.append(float(input()))
    matriz.append(sub)
k=0
soma=0
for i in range(0,12):
    for j in range(len(matriz[i])-i,len(matriz[i])):
        soma+=matriz[i][j]
        k+=1
if op=='S':
    print("%.1f"%soma)
else: print("%.1f"%(soma/k))