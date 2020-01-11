while 1:
    try:
        v,t = input().split(' ')
        v=int(v)
        t=int(t)
        s=v*2*t
        print(s)
    except EOFError:
        break