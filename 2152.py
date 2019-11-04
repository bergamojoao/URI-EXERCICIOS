n = int(input())
i=0
while i<n:
    x,y,o = input().split(' ')
    x=int(x)
    y=int(y)
    o=int(o)
    if o==0:
        print("%02d:%02d - A porta fechou!"%(x,y))
    else: print("%02d:%02d - A porta abriu!"%(x,y))
    i+=1