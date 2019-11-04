n = -1
base = -1
count =1
countStr=""
j=1

def countFib(n:int):
    if(n==0):
        return
    elif(n==1):
        return
    else:
        countFib(n-1)
        countFib(n-2)
        global count
        count+=2


while(n != 0 or base != 0):
    nStr,baseStr = input().split(' ')
    n = int(nStr,10)
    base = int(baseStr,10)
    count=1
    countStr=""
    countFib(n)
    countStr = str(count)
    print("Case "+str(j)+": "+str(n)+" "+str(base)+" "+str((int(countStr[len(countStr)-1],10)%base)))
    j+=1

