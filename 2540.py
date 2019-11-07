while True:
    try:
        n = int(input())
        votos = input().split(' ')
        pros=0
        for v in votos:
            if v =='1':
                pros+=1
        if pros>=n*(2/3):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break