i=1
j=7
fix=7
cont=0
while(i<=9):
    print("I=%d J=%d"%(i,j))
    if(cont==2):
        cont=0
        i+=2
        fix+=2
        j=fix
    else:
        j-=1
        cont+=1
    