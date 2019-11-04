x=int(input())
z=int(input())
i=0
soma=0
while x>=z:
    z=int(input())
while soma<=z:
    soma+=x
    x+=1
    i+=1
print(i)