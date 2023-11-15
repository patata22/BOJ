n,k=map(int,input().split())

distance=[[float('inf')]*n for i in range(n)]
for i in range(n):
    distance[i][i]=0
for _ in range(k):
    a,b=map(lambda x: int(x)-1,input().split())
    distance[a][b]=1
    distance[b][a]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

answer='Small World!'
for i in range(n):
    for j in range(n):
        if distance[i][j]>6: answer='Big World!'
print(answer)
       