n = int(input())
qin=0
qout=0
j=0
while j<n:
    x = int(input())
    if(x>=10 and x<=20):
        qin+=1
    else: qout+=1
    j+=1
print(str(qin)+" in\n"+str(qout)+" out")