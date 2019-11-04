k = int(input())
i=0
while i<k:
    nStr,mStr = input().split(' ')
    soma=0
    n=int(nStr)
    m=int(mStr)
    if(n>m):
        aux=m
        m=n
        n=aux
    n+=1
    while(n<m):
        if n%2!=0:
            soma+=n
        n+=1
    print(soma)
    i+=1