n = int(input())
while n>0:
    x,y = input().split(' ')
    x=int(x)
    y=int(y)
    r = pow((3*x),2) + pow(y,2)
    b = 2 * pow(x,2) +  pow(5*y,2)
    c = -100*x+pow(y,3)
    if r>b and r>c:
        print("Rafael ganhou")
    elif c>r  and c>b:
        print("Carlos ganhou")
    elif b>r and b>c:
        print("Beto ganhou")
    n-=1