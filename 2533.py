while True:
    try:
        m = int(input())
        soma1=0
        soma2=0
        while m>0:
            n,c = input().split(' ')
            soma1+=int(n)*int(c)
            soma2+=int(c)
            m-=1
        print("%.4f"%(soma1/(soma2*100)))
    except EOFError:
        break