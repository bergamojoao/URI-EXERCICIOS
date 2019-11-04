while True:
    try:
        a,b = input().split(' ')
        a=int(a)
        b=int(b)
        if a==b:
            print(0)
        else: print(abs(b-a)-1)
    except EOFError:
        break