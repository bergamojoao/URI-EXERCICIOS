op=1
while(op!=2):
    val=0
    notas=[0,0]
    while val<2:
        n =float(input())
        if(n>=0 and n<=10):
            notas[val]=n
            val+=1
        else:print("nota invalida")
    media =round((notas[0]+notas[1])/2,2)
    print("media = %.2f" % media)
    print("novo calculo (1-sim 2-nao)")
    op=int(input())
    while(op!=1 and op!=2):
        print("novo calculo (1-sim 2-nao)")
        op=int(input())
