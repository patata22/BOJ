n=int(input())
lines=[tuple(map(int,input().split())) for i in range(n)]
distance=[[float('inf')]*n for i in range(n)]

for i in range(n):
    l1,r1=lines[i]
    for j in range(n):
        l2,r2=lines[j]
        if i==j:
            distance[i][j]=0
            continue
        if max(r1,r2)-min(l1,l2)<=r1+r2-l1-l2: distance[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

for _ in range(int(input())):
    a,b=map(lambda x: int(x)-1, input().split())
    answer=distance[a][b]
    if answer==float('inf'):print(-1)
    else: print(answer)
        