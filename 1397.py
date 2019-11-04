n = int(input())
while n!=0:
    a=0
    b=0
    while n>0:
        x,y= input().split(' ')
        x=int(x)
        y=int(y)
        if x>y:
            a+=1
        elif y>x:
            b+=1
        n-=1
    print("%d %d"%(a,b))
    n=int(input())
