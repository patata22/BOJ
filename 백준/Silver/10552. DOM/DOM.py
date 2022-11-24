import sys
input= sys.stdin.readline
    

n,m,now = map(int,input().split())
graph = [0]*(m+1)
turn = 0
for _ in range(n):
    a,b = map(int,input().split())
    if not graph[b]: graph[b] = a

visited = [0]*(m+1)

inf = 0
while graph[now]:
    turn +=1
    if visited[now]:
        inf=1
        break
    visited[now] = 1
    now = graph[now]
if inf: print(-1)
else: print(turn)
