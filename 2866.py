n = int(input())
while n>0:
    frase = input()
    resul=""
    for i in range(len(frase)-1,-1,-1):
        if frase[i].islower():
            resul+=frase[i]
    print(resul)
    n-=1