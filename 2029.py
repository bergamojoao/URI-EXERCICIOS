while True:
    try:
        v, d = float(input("")), float(input(""))
        a = 3.14*(d/2)**2
        print("ALTURA = %.2f\nAREA = %.2f" %(v/a, a))
    except EOFError:
        break