n = int(input())
i=0
valores=input()
valores=valores.split(' ')
v=[]
while(i<n):
    v.append(int(valores[i]))
    i+=1
i=0
menor=0
pMenor=0
while(i<n):
    if i==0:
        menor=v[i]
    else:
        if v[i]<menor:
            menor=v[i]
            pMenor=i
    i+=1
print("Menor valor: %d"%menor)
print("Posicao: %d"%pMenor)
        

