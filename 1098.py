i=0.0
j=1.0
cont=0
while(i<=2):
    if i==0 or i==1 or (i>1.9 and i<2.1):
        print("I=%.0f J=%.0f"%(i,j+i))
    else:print("I=%.1f J=%.1f"%(i,j+i))
    cont+=1
    j+=1
    if(cont==3):
        j=1
        i+=0.2
        cont=0
