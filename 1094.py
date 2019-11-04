n = int(input())
i=0
total=0 
cobaias ={"C":0,"S":0,"R":0}
while i<n:
    qtdStr,tipo = input().split(' ')
    qtd = int(qtdStr)
    total+=qtd
    cobaias[tipo]+=qtd
    i+=1
print("Total: %d cobaias"%total)
print("Total de coelhos: %d"%cobaias["C"])
print("Total de ratos: %d"%cobaias["R"])
print("Total de sapos: %d"%cobaias["S"])
print("Percentual de coelhos: %.2f"% ((cobaias["C"]/total)*100)+" %")
print("Percentual de ratos: %.2f"% ((cobaias["R"]/total)*100)+" %")
print("Percentual de sapos: %.2f"% ((cobaias["S"]/total)*100)+" %")
