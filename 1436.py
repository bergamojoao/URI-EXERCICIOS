import statistics
n = int(input())
i=1
while i<=n:
    linha = input().split(' ')
    for l in linha:
        l=int(l)
    print("Case %d: %s"%(i,statistics.median_low(linha)))
    i+=1
