import math
f1=(1+math.sqrt(5))/2
f2=(1-math.sqrt(5))/2
n = int(input())
resul = (pow(f1,n)-pow(f2,n))/math.sqrt(5)
print("%.1f"%resul)