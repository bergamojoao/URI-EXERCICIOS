cpf = input()
linha=""
for i in range(0,len(cpf)):
    if cpf[i]!='.' and cpf[i]!='-':
        linha+=cpf[i]
    else:
        print(linha)
        linha=""
    if i==len(cpf)-1:
        print(linha)
