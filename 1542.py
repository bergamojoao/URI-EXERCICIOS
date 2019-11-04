while True:
    try:
        Q,D,P = input().split(' ')
        Q=int(Q)
        D=int(D)
        P=int(P)
        pages = (Q * D * P) / (P - Q)
        if pages<=1:
            print("%d pagina"%pages)
        else:
            print("%d paginas"%pages)
    except:
        break