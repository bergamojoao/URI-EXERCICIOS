n = int(input())
while n>0:
    a,b = input().split(' ')
    string =""
    maior=len(a)
    if len(b)>len(a):
        maior = len(b)
    for i in range(0,maior):
        if len(a)>i:
            string+=a[i]
        if len(b)>i:
            string+=b[i]
    print(string)
    n-=1