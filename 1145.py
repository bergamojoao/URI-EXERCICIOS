x,y=input().split(" ")
x=int(x)
y=int(y)
i=1
while i<=y:
    k=x
    linha=""
    while(k>0):
        if k!=x:
            linha+=" "
        linha+=str(i)
        i+=1
        k-=1
    print(linha)