n = int (input())
k=0
while n>0:
    i=0
    palavras=[]
    maxP=0
    if k!=0:
        print()
    while i<n:
        palavras.append(input())
        if len(palavras[i])>maxP:
            maxP=len(palavras[i])
        i+=1
    for k in range(0,len(palavras)):
        space = maxP-len(palavras[k])
        while space>0:
            print(" ",end="")
            space-=1
        print(palavras[k])
    k+=1
    n = int (input())