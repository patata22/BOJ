from collections import deque

def sol(x):
    q=deque()
    q.append(x)
    visited[x]=1
    team=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if team: teamA.append(now)
            else: teamB.append(now)
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    q.append(to)
        team=1-team

n=int(input())

graph=[[] for i in range(n+1)]
for a in range(1,n+1):
    temp=list(map(int,input().split()))
    for j in range(1,len(temp)):
        b=temp[j]
        graph[a].append(b)


visited=[0]*(n+1)
teamA=[]
teamB=[]

for i in range(1,n+1):
    if not visited[i]:
        sol(i)
teamA.sort()
teamB.sort()
print(len(teamA))
print(*teamA)
print(len(teamB))
print(*teamB)
