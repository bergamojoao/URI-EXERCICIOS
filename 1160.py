n = int(input())

while n>0:
    pA,pB,cA,cB = input().split(' ')
    pA=float(pA)
    pB=float(pB)
    cA=float(cA)
    cB=float(cB)
    i=0
    while pA<=pB:
        pA+=int((cA/100)*pA)
        pB+=int((cB/100)*pB)
        i+=1
        if i>100:
            break
    if i>100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos."%i)
    n-=1

    
    
    