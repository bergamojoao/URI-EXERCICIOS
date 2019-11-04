linha = int(input())
op = str(input())
matriz=[]

for i in range(0,12):
    matriz.append([])
    for j in range(0,12):
        matriz[i].append(float(input()))
soma=0
for k in matriz[linha]:
    soma+=k
if(op=="S"):
    print(soma)
elif(op=="M"):
    print(soma/12)