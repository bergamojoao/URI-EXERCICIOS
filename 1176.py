fib = []
fib.append(0)
fib.append(1)
n=int(input())
cont=0
while(cont<n):
    i=int(input())
    if len(fib)>i:
        print("Fib(%d) = %d"%(i,fib[i]))
    else:
        k=len(fib)
        while k<=i:
            fib.append(fib[k-2]+fib[k-1])
            k+=1
        print("Fib(%d) = %d"%(i,fib[i]))
    cont+=1


