a,b,c = input().split(' ')
a=int(a)
b=int(b)
c=int(c)

if a==b or b==c or c==a :
    print("S")
elif a == b+c or c == b+a or b == a+c:
    print("S")
else: print("N")
