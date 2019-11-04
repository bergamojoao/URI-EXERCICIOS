n = int(input())
i=0
musicas=[]
musicas.append("PROXYCITY")
musicas.append("P.Y.N.G.")
musicas.append("DNSUEY!")
musicas.append("SERVERS")
musicas.append("HOST!")
musicas.append("CRIPTONIZE")
musicas.append("OFFLINE DAY")
musicas.append("SALT")
musicas.append("ANSWER!")
musicas.append("RAR?")
musicas.append("WIFI ANTENNAS")
while i<n:
    x,y = input().split(' ')
    x=int(x)
    y=int(y)
    print(musicas[x+y])
    i+=1