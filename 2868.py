n = int(input())
while n>0:
    a,op,b,lixo,resul = input().split(' ')
    a=int(a)
    b=int(b)
    resul=int(resul)
    correto=0
    if op=='+':
        correto=a+b
    elif op=='-':
        correto=a-b
    else:
        correto=a*b
    print("E",end="")
    for i in range(0,abs(correto-resul)):
        print("r",end="")
    print("ou!")
    n-=1
    