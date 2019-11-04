num = input() # input do usuario
##############################################################
unidades = ["I","II","III","IV","V","VI","VII","VIII","IX"]
dezenas = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
centenas = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
milhares = ["M","MM","MMM"]
sequencia = ["I","V","X","L","C","D","M"] # sequencia crescente dos algarismos existentes
##############################################################
val = int(num)
if(val>0 and val<4000): # se esta dentro da representacao dos romanos
    romano=str()
    milhar = int(val / 1000) # recebe a parte "milhar" do numero
    if(milhar!=0):
        val=(val%1000)
        romano+=str(milhares[milhar-1]) # concatena o algarismo de milhar necessario
    centena = int(val/100)  # recebe a parte "centena" do numero
    if(centena!=0):
        val=(val%100)
        romano+=str(centenas[centena-1]) # concatena algarismo de centena necessario
    dezena=int(val/10) # recebe a parte "dezena" do numero
    if(dezena!=0):
        val=(val%10)
        romano+=str(dezenas[dezena-1]) # concatena algarismo de dezena necessario
    unidade=int(val) # recebe a parte "unidade" do numero
    if(unidade!=0):
        romano+=str(unidades[unidade-1]) # concatena algarismo de unidade necessario
    print(romano)