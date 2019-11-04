i=0
while i<10:
    x = int(input())
    if x<=0:
        print("X[%d] = 1"%i)
    else:
        print("X[%d] = %d"%(i,x))
    i+=1