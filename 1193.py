n = int(input())
k=1
while n>=k:
    i,t = input().split(' ')
    print("Case %d"%k)
    if t=="bin":
        a = int(i,2)
        print("%d dec"%a)
        print("%x hex"%a)
    elif t=="dec":
        a = int(i)
        b=bin(a)
        c=b[2:len(b)]
        print("%x hex"%a)
        print("%s bin"%c)
    elif t=="hex":
        a = int(i,16)
        b=bin(a)
        c=b[2:len(b)]
        print("%d dec"%a)
        print("%s bin"%c)
    print()
    k+=1