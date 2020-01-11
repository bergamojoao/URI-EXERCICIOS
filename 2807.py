n = int(input())
seq = []
while len(seq) != n:
    t = len(seq)
    if t<2:
        seq.append(1)
    else:
        seq.append(seq[t-1]+seq[t-2])
seq.reverse()
for i in range(0,len(seq)):
    if i!=len(seq)-1:
        print(seq[i],end=' ')
    else: print(seq[i])