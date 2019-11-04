n = int(input())
i=0
while i<n:
    x,y=input().split(' ')
    x=int(x)
    y=int(y)
    j=0
    soma=0
    while j<y:
        if x%2==1:
            soma+=x
            j+=1
        x+=1
    print(soma)      
    i+=1