n = int(input())
i=0
casa=0
escritorio=0
while i<n:
    ida,volta = input().split(' ')
    if(ida=="chuva"):
        escritorio+=1
        if(casa!=0):
            casa-=1
    if(volta=="chuva"):
        if(escritorio!=0):
            escritorio-=1
        casa+=1
    i+=1
print("%d %d"%(casa,escritorio))
