n = int(input())
while n>0:
    k = float(input())
    i=0
    while k>1:
        k/=2
        i+=1
    print("%d dias"%i)
    n-=1
