n = int(input())
i=0
anoes=0
elfos=0
humanos=0
magos=0
xhobits=0
while i<n:
    lixo,t = input().split(' ')
    if t=='A':
        anoes+=1
    elif t=='E':
        elfos+=1
    elif t=='H':
        humanos+=1
    elif t=='M':
        magos+=1
    elif t=='X':
        xhobits+=1
    i+=1
print("%d Hobbit(s)"%xhobits)
print("%d Humano(s)"%humanos)
print("%d Elfo(s)"%elfos)
print("%d Anao(s)"%anoes)
print("%d Mago(s)"%magos)
