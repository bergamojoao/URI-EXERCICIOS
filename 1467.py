while True:
    try:
        a,b,c = input().split(' ')
        if a==b and b==c:
            print("*")
        elif a==b and b!=c:
            print("C")
        elif a==c and b!=a:
            print("B")
        else:print("A")
    except EOFError:
        break