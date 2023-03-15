n=int(input())
temp=list(input().split())
gene=set()
double=set()
for x in temp:
    if x in gene: double.add(x)
    else: gene.add(x)
answer=set()
gene=list(gene)

for i in range(len(gene)):
    a=gene[i]
    for j in range(len(gene)):
        if (i==j and a in double) or i!=j:
            b=gene[j]
            answer.add(chr(max(ord(a[0]),ord(b[1]))))
print(len(answer))
print(*sorted(list(answer)))
