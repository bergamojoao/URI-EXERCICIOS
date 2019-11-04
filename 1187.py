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
    if i+1<=len(matriz[i])-i-1:
        for j in range(i+1,len(matriz[i])-i-1):
            soma+=matriz[i][j]
            k+=1
    else:break
if op=='S':
    print("%.1f"%soma)
else: print("%.1f"%(soma/k))