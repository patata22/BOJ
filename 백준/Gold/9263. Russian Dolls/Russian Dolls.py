n=int(input())

doll=[tuple(map(int,input().split())) for i in range(n)]

doll.sort(key=lambda x: -x[2])

used=[0]*n
answer=0
for i in range(n):
    oo,ii,c=doll[i]
    maxSize=0
    target=-1
    for j in range(n):
        if used[j] or i==j: continue
        outside,inside,cost=doll[j]
        if ii>outside and maxSize<outside:
            maxSize=outside
            target=j
    if target!=-1: used[target]=1
    answer+=c*(ii-maxSize)

print(answer)
