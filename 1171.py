n = int(input())
array={}
while n>0:
    s = input()
    if not s in array:
        array[s]=1
    else: array[s]+=1
    n-=1
aux = array.keys()
chaves=[]
for k in aux:
    chaves.append(int(k)) # transforma chaves em int para ordenar
chaves.sort()
for k in chaves:
    print("%d aparece %d vez(es)"%(k,array[str(k)]))
