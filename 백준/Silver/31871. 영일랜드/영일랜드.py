import sys
input=sys.stdin.readline

def sol(depth,now,dist):
    if depth==n:
        global answer
        if distance[now][0]!=-1:
            answer=max(answer,dist+distance[now][0])
        return
    for to in range(1,n+1):
        if not visited[to] and distance[now][to]!=-1:
            visited[to]=1
            sol(depth+1,to,dist+distance[now][to])
            visited[to]=0
            
n=int(input())
distance=[[-1]*(n+1) for i in range(n+1)]
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    distance[a][b]=max(distance[a][b],c)
visited=[0]*(n+1)

answer=-1
sol(0,0,0)
print(answer)
