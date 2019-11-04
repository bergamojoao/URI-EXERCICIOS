x = int(input())
y = int(input())
if(x>y):
    ant =y
    y=x
    x=ant
z=x+1
while(z<y):
    if(z % 5 == 2 or z % 5 == 3):
        print(z)
    z+=1