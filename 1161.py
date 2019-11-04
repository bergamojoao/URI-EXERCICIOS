import math
while True:
    try:
        x,y = input().split(' ')
        x=int(x)
        y=int(y)
        print(math.factorial(x)+math.factorial(y))
    except EOFError:
        break