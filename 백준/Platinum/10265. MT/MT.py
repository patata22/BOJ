import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)

from collections import deque

def make_team(now):
    visited[now] = 1
    to = graph[now]
    if visited[to]:
        if not finished[to]:
            temp = 1
            while to!=now:
                to = graph[to]
                temp+=1
            t= bfs(to)
            team.append((temp, t))
    else:
        make_team(to)
    finished[now]=1

def bfs(now):
    q=deque()
    q.append(now)
    t = 1
    visited_temp = [0]*(n+1)
    visited_temp[now]=1
    while q:
        now = q.popleft()
        for to in graph_reverse[now]:
            if not visited_temp[to]:
                t+=1
                visited_temp[to]=1
                q.append(to)
    return t

n,k = map(int,input().split())
graph = [0]+list(map(int,input().split()))
graph_reverse= [[] for i in range(n+1)]
for i in range(1,n+1):
    graph_reverse[graph[i]].append(i)
team= []
visited = [0]*(n+1)
finished = [0]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        make_team(i)

N = len(team)
knap = [[0]*(k+1) for i in range(N)]
for i in range(N):
    number,t= team[i]
    for j in range(1,k+1):
        knap[i][j] = knap[i-1][j]
        for z in range(number, t+1):
            if j-z>=0: knap[i][j] = max(knap[i][j], knap[i-1][j-z]+z)
print(knap[-1][-1])
        
