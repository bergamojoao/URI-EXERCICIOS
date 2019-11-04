v=[]
n=20
while n>0:
    a = int(input())
    v.append(a)
    n-=1
aux = v[::-1]
for i in range(0,len(aux)):
    print("N[%d] = %d"%(i,aux[i]))
