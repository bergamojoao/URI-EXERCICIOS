while True:
    try:
        n = int(input())
        linhas = input().split(' ')
        inteiros = []
        for l in linhas:
            inteiros.append(int(l))
        maior=0
        for i in inteiros:
            if i>maior:
                maior=i
        if maior<10:
            print(1)
        elif maior>=10 and maior<20:
            print(2)
        else: print(3)
    except EOFError:
        break