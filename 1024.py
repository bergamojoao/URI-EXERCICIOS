n = int(input())

while n>0:
    word = input()
    new=""
    new2=""
    new3=""
    for i in range(0,len(word)):
        k=ord(word[i])
        if (ord(word[i])>=65 and ord(word[i])<=90) or (ord(word[i])>=97 and ord(word[i])<=122):
            k+=3
        new+=chr(k)
    new2=new[::-1]
    for i in range(0,int(len(word)/2)):
        new3+=new2[i]
    for i in range(int(len(word)/2),len(word)):
        k=ord(new2[i])
        k-=1
        new3+=chr(k)
    print(new3)
    n-=1
