n,m=map(int,input().split())

distance=[[float('inf')]*n for i in range(n)]
for i in range(n): distance[i][i]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    distance[a-1][b-1]=c
    distance[b-1][a-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

total=float('inf')
answer=0
for i in range(n):
    if sum(distance[i])<total:
        total=sum(distance[i])
        answer=i
        
print(answer+1)
