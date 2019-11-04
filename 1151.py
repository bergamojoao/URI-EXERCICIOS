ant1=0
ant2=1
atual=1
i=3
n=int(input())
resul="0 1 "
while(i<=n):
    atual=ant1+ant2
    if(i!=3):
        resul+=" "
    resul+=str(atual)
    ant1=ant2
    ant2=atual
    i+=1
print(resul)