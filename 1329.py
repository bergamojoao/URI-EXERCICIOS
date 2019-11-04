n = int(input())
while n!=0:
    mary=0
    john=0
    linha = input().split(' ')
    for i in linha:
        if i=='0':
            mary+=1
        else: john+=1
    print("Mary won %d times and John won %d times"%(mary,john))
    n = int(input())

