i=0
v=[]
while i<100:
    v.append(float(input()))
    i+=1
i=0
while i<100:
    if v[i]<=10:
        print("A[%d] = %.1f"%(i,v[i]))
    i+=1