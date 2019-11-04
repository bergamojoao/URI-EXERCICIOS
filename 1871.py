x,y = input().split(' ')
x=int(x)
y=int(y)
while x!=0 and y!=0:
    s = str(x+y)
    for c in s:
        if c!='0':
            print(c,end='')
    print()
    x,y = input().split(' ')
    x=int(x)
    y=int(y)