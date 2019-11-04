val=0
notas=[0,0]
while val<2:
    n =float(input())
    if(n>=0 and n<=10):
        notas[val]=n
        val+=1
    else:print("nota invalida")
print("media = "+str((notas[0]+notas[1])/2))