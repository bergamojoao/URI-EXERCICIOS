n = int(input())
i=0
j=0
while(i<1000):
    if j==n:
        j=0
    else:
        print("N[%d] = %d"%(i,j))
        j+=1
        i+=1