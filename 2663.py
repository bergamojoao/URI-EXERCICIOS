n = int(input())
i=0
vagas=int(input())
pontos=[]
while i<n:
    pontos.append(int(input()))
    i+=1
pontos.sort(reverse=True)
i=0
pEmpate=0
i=vagas-1
while i<n-1:
    if pontos[i]==pontos[i+1]:
        vagas+=1
    else: break
    i+=1
print(vagas)

