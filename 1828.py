n = int(input())
i=1
while i<=n:
    a,b = input().split(' ')
    if a==b:
        print("Caso #%d: De novo!"%i)
    elif a=="tesoura" and b=="papel":
        print("Caso #%d: Bazinga!"%i)
    elif a=="papel" and b=="pedra":
        print("Caso #%d: Bazinga!"%i)
    elif a=="pedra" and b=="lagarto":
        print("Caso #%d: Bazinga!"%i)
    elif a=="lagarto" and b=="Spock":
        print("Caso #%d: Bazinga!"%i)
    elif a=="Spock" and b=="tesoura":
        print("Caso #%d: Bazinga!"%i)
    elif a=="tesoura" and b=="lagarto":
        print("Caso #%d: Bazinga!"%i)
    elif a=="lagarto" and b=="papel":
        print("Caso #%d: Bazinga!"%i)
    elif a=="papel" and b=="Spock":
        print("Caso #%d: Bazinga!"%i)
    elif a=="Spock" and b=="pedra":
        print("Caso #%d: Bazinga!"%i)
    elif a=="pedra" and b=="tesoura":
        print("Caso #%d: Bazinga!"%i)
    else:
        print("Caso #%d: Raj trapaceou!"%i)
    i+=1
