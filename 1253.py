alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
while n>0:
    word = input()
    chave = int(input())
    resul=""
    for w in word:
        if w in alfabeto:
            k = alfabeto.find(w)
            k-=chave
        if k>=len(alfabeto):
            k-len(alfabeto)
        resul+=alfabeto[k]
    print(resul)
    n-=1
    
    
