import sys
input=sys.stdin.readline

n,m=map(int,input().split())
distance=[[float('inf')]*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    distance[a][b]=c

for k in range(1,n+1):
    distance[k][k]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
answer=float('inf')
for i in range(1,n+1):
    for j in range(i+1,n+1):
        answer=min(answer, distance[i][j]+distance[j][i])
if answer==float('inf'):print(-1)
else:print(answer)
    
