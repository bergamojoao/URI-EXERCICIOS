x,y = input().split(' ')
while x !='0' and y!='0':
    resul=""
    for s in y:
        if s!=x:
            resul+=s
    if resul!="":
        resul=int(resul)
    else: resul=0
    print(resul)
    x,y = input().split(' ')
