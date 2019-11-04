nStr =input()
n = float(nStr)
if(n==0 and nStr[0]=='-'):
    resul="%.4E"%n
elif(n>=0):
    resul="+%.4E"%n
else:resul="%.4E"%n
print(resul)
