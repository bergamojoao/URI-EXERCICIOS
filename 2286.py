n = int(input())
i=1
while n>=i:
    nome1 = input()
    nome2 = input()
    j=0
    while j<n:
        a,b=input().split(' ')
        a=int(a)
        b=int(b)
        if j==0:
            print("Teste %d"%i)
        if (a+b)%2==0:
            print(nome1)
        else:
            print(nome2)
        j+=1
    print()
    i+=1
    n=int(input())