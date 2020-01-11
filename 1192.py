def numeros_obtidos(s):
    a, b = int(s[0]), int(s[2])
    c = s[1]
    if a == b:
        return a * b
    if c.isupper():
        return b - a
    else:
        return a + b

t = int(input())
for _ in range(t):
    s = input()
    print(numeros_obtidos(s))