a,c,q,sc = input().split(' ')
a=int(a)
c=int(c)
q=int(q)
sc=int(sc)
resul = c-q-sc-1
if a<=resul:
    print("Igor feliz!")
else:
    if q>sc/2:
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")