n = int(input())
i=0
def isPerfeito(n):
    soma=0
    if(n==1):
        return False
    if(n==0):
        return False
    for i in range(1,n):
        if(n%i==0):
            soma+=i
    if(soma==n):
        return True
    else: return False
while(i<n):
    p = int(input())
    if isPerfeito(p):
        print("%d eh perfeito"%p)
    else: print("%d nao eh perfeito"%p)
    i+=1