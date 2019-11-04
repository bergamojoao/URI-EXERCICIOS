n = int(input())
while n>0:
    a,b,c = input().split(' ')
    a=int(a)
    b=int(b)
    c=int(c)
    delta = pow(b,2) - (4*a*c)
    r = -(delta/(4*a))
    print("%.2f"%r)
    n-=1