op=0
vInter=0
vGremio=0
empates=0
cont=0
while op!=2:
    gInter,gGremio = input().split(" ")
    gInter=int(gInter)
    gGremio=int(gGremio)
    if gInter>gGremio:
        vInter+=1
    elif gGremio>gInter:
        vGremio+=1
    else: empates+=1
    cont+=1
    print("Novo grenal (1-sim 2-nao)")
    op = int(input())
print(str(cont)+" grenais")
print("Inter:%d"%vInter)
print("Gremio:%d"%vGremio)
print("Empates:%d"%empates)
if vInter>vGremio:
    print("Inter venceu mais")
elif vGremio>vInter:
    print("Gremio venceu mais")
else: print("Nao houve vencedor")


