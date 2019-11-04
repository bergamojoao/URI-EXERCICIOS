n =int(input())
matMaior=0
medMaior=0
while n>0:
    mat,media = input().split(' ')
    media=float(media)
    if media>=8:
        if media>medMaior:
            medMaior=media
            matMaior=mat
    n-=1
if medMaior>0:
    print(matMaior)
else: print("Minimum note not reached")
    
