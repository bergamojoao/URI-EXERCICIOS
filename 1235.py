n = int(input())
while n>0:
    s = input()
    a=""
    for i in range(0,int(len(s)/2)):
        a=s[i]+a
    b=""
    for i in range(int(len(s)/2),len(s)):
        b=s[i]+b
    print("%s%s"%(a,b))
    n-=1
