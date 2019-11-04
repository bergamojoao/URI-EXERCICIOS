x,y,z = input().split(' ')
x=int(x)
y=int(y)
z=int(z)
t=x+y+z
if t>=24:
    t-=24
elif t<0:
    t=24+t
print(t)