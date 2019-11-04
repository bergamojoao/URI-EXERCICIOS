valor = float(input())
if valor<=2000:
    print("Isento")
elif valor>2000 and valor<=3000:
    valor=(valor-2000)*0.08
    print("R$ %.2f"%valor)
elif valor>3000 and valor<=4500:
    valor=(valor-3000)*0.18+80
    print("R$ %.2f"%valor)
else: 
    valor=(valor-4500)*0.28+350
    print("R$ %.2f"%valor)