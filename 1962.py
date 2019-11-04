n = int(input())
i=0
while i<n:
    ano = int(input())
    ano=2015-ano
    if ano<=0:
        print("%d A.C."%(ano*-1+1))
    else:
        print("%d D.C."%(ano))
    i+=1