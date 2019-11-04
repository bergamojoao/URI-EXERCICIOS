while True:
    try:
        a,b = input().split(' ')
        a=bin(int(a))
        a1=a[2:len(a)]
        b=bin(int(b))
        b1=b[2:len(b)]
        an = ""
        resul=""
        if len(a1)==len(b1):
            for i in range(0,len(a1)):
                if a1[i]==b1[i]:
                    resul+='0'
                else:
                    resul+='1'
        elif len(a1)>len(b1):
            j=0
            for i in range(0,len(a1)):
                if i<len(a1)-len(b1):
                    resul+=a1[i]
                else:
                    if (a1[i]==b1[j]):
                        resul+='0'
                    else:
                        resul+='1'
                    j+=1
        else:
            j=0
            for i in range(0,len(b1)):
                if i<len(b1)-len(a1):
                    resul+=b1[i]
                else:
                    if (b1[i]==a1[j]):
                        resul+='0'
                    else:
                        resul+='1'
                    j+=1  
        print(int(resul,2))
    except EOFError:
        break
