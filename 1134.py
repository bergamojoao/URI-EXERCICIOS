n=0
valores = [0,0,0]
while(n!=4):
    n = int(input())
    if(n<=3):
        valores[n-1]+=1
print("MUITO OBRIGADO")
print("Alcool: %d"%valores[0])
print("Gasolina: %d"%valores[1])
print("Diesel: %d"%valores[2])