n = int(input())
i=0
def isPrimo(n):
    if(n==1):
        return True
    if(n==2):
        return True
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

while(i<n):
    p = int(input())
    if isPrimo(p):
        print("%d eh primo"%p)
    else: print("%d nao eh primo"%p)
    i+=1


