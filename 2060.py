n = int(input())
i=0
numeros = input().split(' ')
m2=0
m3=0
m4=0
m5=0
while i<n:
    a = int(numeros[i])
    if a%2==0:
        m2+=1
    if a%3==0:
        m3+=1
    if a%4==0:
        m4+=1
    if a%5==0:
        m5+=1
    i+=1
print("%d Multiplo(s) de 2"%m2)
print("%d Multiplo(s) de 3"%m3)
print("%d Multiplo(s) de 4"%m4)
print("%d Multiplo(s) de 5"%m5)
