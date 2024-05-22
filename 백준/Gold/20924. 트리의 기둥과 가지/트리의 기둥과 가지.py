from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    q.append((r,0))
    visited[r]=1
    giga=True
    while q and giga:
        now,dist=q.popleft()
        cnt=0
        for to,d in graph[now]:
            if not visited[to]:
                visited[to]=1
                cnt+=1
                q.append((to,dist+d))
        if cnt!=1:
            giga=False
            answer1=dist
    
    if q:
        answer2=0
        while q:
            now,dist=q.popleft()
            answer2=max(answer2,dist)
            for to,d in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    cnt+=1
                    q.append((to,dist+d))
        return answer1,answer2-answer1
    else: return answer1,0
        
        

n,r=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited=[0]*(n+1)

print(*sol())
