while True:
    try:
        palavras = input().split(' ')
        cont=0
        seq=0
        for i in range(0,len(palavras)-1):
            palavras[i]=palavras[i].upper()
            palavras[i+1]=palavras[i+1].upper()
            if palavras[i][0]==palavras[i+1][0] and seq<1:
                cont+=1
                seq+=1
            elif palavras[i][0]!=palavras[i+1][0]: seq=0
        print(cont)
    except EOFError:
        break
