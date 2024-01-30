n,m=map(int,input().split())
distance=[[float('inf')]*n for i in range(n)]
for _ in range(m):
    a,b=map(lambda x: int(x)-1,input().split())
    distance[a][b]=1
    distance[b][a]=1

for k in range(n):
    distance[k][k]=0
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

D=float('inf')
answer=[]

for i in range(n):
    for j in range(i+1,n):
        temp=0
        for k in range(n):
            temp+=min(distance[i][k],distance[j][k])

        if temp*2<D:
            D=temp*2
            answer=[i+1,j+1]

print(*answer,D)
