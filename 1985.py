n = int(input())
i=0
total=0
while i<n:
    op,qtd = input().split(' ')
    op=int(op)
    qtd=int(qtd)
    if op==1001:
        total+=qtd*1.50
    elif op==1002:
        total+=qtd*2.50
    elif op==1003:
        total+=qtd*3.50
    elif op==1004:
        total+=qtd*4.50
    elif op==1005:
        total+=qtd*5.50
    i+=1
print("%.2f"%total)
