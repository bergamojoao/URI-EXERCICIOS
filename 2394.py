comp,voltas = input().split(' ')
comp=int(comp)
voltas=int(voltas)
tempos=[]
while comp>0:
    c = input().split(' ')
    soma=0
    for t in c:
        soma+=int(t)
    tempos.append(soma)
    comp-=1
menor=0
index=0
for i in range(0,len(tempos)):
    if i==0:
        menor=tempos[i]
    elif tempos[i]<menor:
        menor=tempos[i]
        index=i
print(index+1)