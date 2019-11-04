while True:
    try:
        exp = input()
        abre=0
        fecha=0
        aux=False
        for l in exp:
            if l=='(':
                abre+=1
            elif l==')':
                fecha+=1
            if fecha!=0 and fecha>abre:
                print("incorrect")
                aux=True
                break
        if not aux:
            if abre==fecha:
                print("correct")
            else: print("incorrect")
    except EOFError:
        break

    