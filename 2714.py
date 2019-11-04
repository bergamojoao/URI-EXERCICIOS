n = int(input())
while n>0:
    ra = input()
    if ra[0]=='R' and ra[1]=='A' and len(ra)==20:
        i=2
        while i<len(ra):
            if ra[i]!='0':
                break
            else: i+=1
        num =""
        if i==len(ra):
            print("INVALID DATA")
        else:
            for j in range(i,len(ra)):
                num+=ra[j]
            print(num)
    else:print("INVALID DATA")
    n-=1