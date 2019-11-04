i=1
maior=-1
pos=-1
while i<=100:
    n = int(input())
    if(n>maior):
        maior=n
        pos=i
    i+=1
print(str(maior)+"\n"+str(pos))