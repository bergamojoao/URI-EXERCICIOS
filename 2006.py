cha = int(input())
correto=0
linha = input().split(' ')
for l in linha:
    l=int(l)
    if l==cha:
        correto+=1
print(correto)