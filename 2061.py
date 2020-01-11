abas,acoes = input().split(' ')
abas=int(abas)
acoes=int(acoes)

while(acoes!=0):
    acao = input()
    if(acao=="fechou"):
        abas+=1
    if(acao=="clicou"):
        abas-=1
    acoes-=1

print(abas)