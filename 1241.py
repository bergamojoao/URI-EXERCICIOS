n = int(input())
while n>0:
    a,b=input().split(' ')
    if(len(a)<len(b)):
        print("nao encaixa")
    else:
        j=0
        encaixa=True
        for i in range(len(a)-len(b),len(a)):
            if a[i]!=b[j]:
                encaixa=False
            j+=1
        if encaixa:
            print("encaixa")
        else: print("nao encaixa")
    n-=1