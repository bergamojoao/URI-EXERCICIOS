n = int(input())
l = ["one","two","three"]
while n>0:
    word = input()
    erro1=0
    erro2=0
    erro3=0
    if len(word)==3:
        for i in range(0,3):
            if l[0][i] != word[i]:
                erro1+=1
            if l[1][i] != word[i]:
                erro2+=1
    else:
        for i in range(0,5):
            if l[2][i]!=word[i]:
                erro3+=1
    if erro1<=1 and len(word)==3:
        print(1)
    elif erro2<=1 and len(word)==3:
        print(2)
    elif erro3<=1:
        print(3)
    n-=1

    
