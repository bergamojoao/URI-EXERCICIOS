maximo = int(input())
a,op,b = input().split(' ')
resul=0
if op=='+':
    resul=int(a)+int(b)
elif op=='*':
    resul=int(a)*int(b)
if resul<=maximo:
    print("OK")
else:
    print("OVERFLOW")