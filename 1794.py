num = int(input())
l1= input().split()
la = int(l1[0])
lb = int(l1[1])
l2= input().split()
sa = int(l2[0])
sb = int(l2[1])
if la <= num <= lb and sa <= num <= sb:
    print("possivel")
else:
    print("impossivel")