def change(x):
    if x=='Y': return 1
    return 0

n=int(input())
d=int(input())

distance=[[float('inf')]*n for i in range(n)]
for i in range(n):
    x=list(input())
    for j in range(i+1,n):
        if x[j]=='Y':
            distance[i][j]=d
            distance[j][i]=d
for i in range(n):
    distance[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

answer=0
for i in range(n):
    for j in range(n):
        answer=max(distance[i][j],answer)
if answer==float('inf'):print(-1)
else: print(answer)
