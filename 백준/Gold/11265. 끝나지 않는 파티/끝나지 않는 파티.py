import sys
input=sys.stdin.readline

n,m=map(int,input().split())

distance=[list(map(int,input().split())) for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][k]+distance[k][j]<distance[i][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

for _ in range(m):
    a,b,c=map(int,input().split())
    print('Enjoy other party') if distance[a-1][b-1]<=c else print('Stay here')
