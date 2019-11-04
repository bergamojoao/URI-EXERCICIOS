soma=0
resul=""
while True:
    nStr,mStr = input().split(' ')
    resul=""
    soma=0
    n=int(nStr)
    m=int(mStr)
    if(n<=0 or m<=0):
        break
    if(n>m):
        aux=m
        m=n
        n=aux
    while(n<=m):
        resul+=str(n)+" "
        soma+=n
        n+=1
    print(resul+"Sum="+str(soma))

