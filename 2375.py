diametro = int(input())
a,l,p = input().split(' ')
a=int(a)
l=int(l)
p=int(p)
if a>=diametro and l>=diametro and p>=diametro:
    print("S")
else: print("N")