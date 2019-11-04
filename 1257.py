n = int(input())
while n>0:
    k= int(input())
    i=0
    soma=0
    while i<k:
        s = input()
        for j in range(0,len(s)):
            soma+=(ord(s[j])-65)+i+j
        i+=1
    print(soma)
    n-=1
