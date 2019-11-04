a=0
N=int(input())
for i in range(1,N+1):
    for k in range(1,4):
        if(k==3):
            print(i**k,end='')
        else: print(i**k,end=' ')
    print()

    for j in range(1,4):
        if j==2 or j==3:
            a=i**j+1
            if(j==3):
                print(a, end='')
            else: print(a, end=' ')
        else:
            print(i**j,end=' ')
        a=0
    print()