n = int(input())
j=0
medias = []
while j<n:
    notasStr = input().split(' ')
    nota1=float(notasStr[0])
    nota2=float(notasStr[1])
    nota3=float(notasStr[2])
    medias.append(round((nota1*2+nota2*3+nota3*5)/10,1))
    j+=1
for m in medias:
    print(m)