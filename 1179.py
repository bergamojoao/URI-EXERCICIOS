n=15
par=[]
impar=[]
while n>0:
    v = int(input())
    if v%2==0:
        par.append(v)
    else: impar.append(v)
    if len(impar) ==5:
        for i in range(0,len(impar)):
            print("impar[%d] = %d"%(i,impar[i]))
        impar=[]
    if len(par)==5:
        for i in range(0,len(par)):
            print("par[%d] = %d"%(i,par[i]))
        par=[]
    n-=1
if len(impar)<5:
    for i in range(0,len(impar)):
        print("impar[%d] = %d"%(i,impar[i]))
if len(par)<5:
    for i in range(0,len(par)):
        print("par[%d] = %d"%(i,par[i]))
