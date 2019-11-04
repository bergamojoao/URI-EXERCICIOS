n = int(input())
while n>0:
    l = input().split(' ')
    l.sort(key=len,reverse=True)
    for i in range(0,len(l)):
        if i==0:
            print("%s"%l[i],end='')
        else:
            print(" %s"%l[i],end='')
    print()
    n-=1